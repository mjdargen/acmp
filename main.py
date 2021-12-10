# acmp (Animal Crossing Music Player) - main.py
# Michael D'Argenio
# mjdargen@gmail.com
# https://dargenio.dev
# https://github.com/mjdargen
import os
import time
import requests
import datetime
import argparse
import multiprocessing
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio


# gets location (lat/lon) based on IP address
def get_location():
    url = 'http://ipinfo.io/json'
    r = requests.get(url)
    data = r.json()
    return data['loc'].split(',')


# gets weather based on lat/lon
# go to https://openweathermap.org/api to register for free API key
# add to .env file like this: WEATHER_KEY=<your_api_key_here>
def get_weather(lat, lon):
    key = os.getenv('WEATHER_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
    r = requests.get(url)
    data = r.json()

    if 'rain' in data['weather'][0]['main'].lower():
        return 'raining'
    elif 'snow' in data['weather'][0]['main'].lower():
        return 'snowing'
    else:
        return 'sunny'


# process for handling timeing to switch over
def timing(conn, ):
    prev = None
    while True:
        # get location
        lat, lon = get_location()
        # get weather
        weather = get_weather(lat, lon)
        # get current time
        now = datetime.datetime.now().strftime("%I%p").lower()
        if now[0] == '0':
            now = now[1:]
        # send message with time and date
        if prev != now:
            conn.send(f'{now}_{weather}')
            prev = now

        # compute how long to sleep for
        now = datetime.datetime.now()
        delta = datetime.timedelta(hours=1)
        next_hour = (now + delta).replace(microsecond=0, second=0, minute=0)
        wait_seconds = (next_hour - now).seconds
        time.sleep(wait_seconds)


# process for handling audio
def audio(conn, game):
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))

    # start with silence to initialize objects before loop
    file = f'{DIR_PATH}/silence.mp3'
    clip = AudioSegment.from_mp3(file)
    playback = _play_with_simpleaudio(clip)

    while True:
        # check for new message
        if conn.poll():
            name = conn.recv()
            print(f'Switching to {name}.')
            file = f'{DIR_PATH}/{game}/{name}.mp3'
            # stop old song and play new one
            playback.stop()
            clip = AudioSegment.from_mp3(file)
            playback = _play_with_simpleaudio(clip)
        # song finished, repeat
        if not playback.is_playing():
            # stop old song and play new one
            playback.stop()
            clip = AudioSegment.from_mp3(file)
            playback = _play_with_simpleaudio(clip)
        time.sleep(2)


def main():
    load_dotenv()

    # handle arguments
    games = ['new-horizons', 'new-leaf', 'wild-world', 'animal-crossing']
    parser = argparse.ArgumentParser(
        description="Animal Crossing Music Player")
    parser.add_argument('--game', dest='game', required=False,
                        help=f'The valid game options are: {", ".join(games)}.')
    args = parser.parse_args()
    if not args.game:
        game = 'new-horizons'
    elif args.game not in games:
        print('Game not recognized... Choosing New Horizons.')
        game = 'new-horizons'
    else:
        game = args.game

    # creating a pipe to communicate between processes
    parent_conn, child_conn = multiprocessing.Pipe()

    # creating processes
    timing_process = multiprocessing.Process(target=timing, args=(child_conn,))
    audio_process = multiprocessing.Process(
        target=audio, args=(parent_conn, game))

    # be sure to kill processes if keyboard interrupted
    try:
        # starting timing process
        timing_process.start()
        # starting audio process
        audio_process.start()

        # wait until audio is finished
        audio_process.join()
        # wait until timing is finished
        timing_process.join()
    except KeyboardInterrupt:
        print('Interrupted')
        audio_process.terminate()
        timing_process.terminate()


if __name__ == '__main__':
    main()

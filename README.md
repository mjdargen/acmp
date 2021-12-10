# acmp - Animal Crossing Music Player
An Animal Crossing hourly music player that you can run in the background on your computer. Takes into account the time of day and weather for music selection!

*Michael D'Argenio  
mjdargenio@gmail.com  
https://dargen.io  
https://github.com/mjdargen  
Created: December 9, 2021*   

For those unfamiliar with the Animal Crossing games, music plays an integral role in creating the atmosphere of the game. Animal Crossing games use the console's system clock to move at and simulate the real passage of time (meaning that when it is 9pm on September 1st in real life, it is 9pm on September 1st in the game). A key way that the developers indicate the passage of time in the game is with the hourly music. In each game, there is a specific song (with slight variations based on weather) for each of the twenty-four hours in a day that repeats for the duration of the hour.

In this project, I created a Python script to play the hourly music in the background on your computer just like in the game. The script uses multiprocessing to handle the various portions of the code. One of the processes handles retrieving the weather and time of day information. The other process handles playing the audio based on the time of day and weather information passed to it. This script is meant to be lightweight so it can run in the background without too much demand.

To run this code in your environment, you will need to:  
   * Install Python 3 and pip (https://www.python.org/).
   * Install ffmpeg for pydub (https://ffmpeg.org/).
   * Install pydub & simpleaudio: `pip3 install -r requirements.txt`
   * Set up an account with OpenWeather and generate an API key (https://openweathermap.org/api).

For a complete walkthrough of how this program works, you can go here: [Instructables Tutorial](https://www.instructables.com/Animal-Crossing-Music-Player/).

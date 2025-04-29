# retrieves audio files
# https://github.com/animal-crossing-music-extension/ac-music-extension
# https://acmusicext.com/static/new-horizons/sunny/5pm.ogg
# https://acmusicext.com/static/kk/aircheck/AC%20-%20Aloha%20K.K..ogg
# snowing/raining/sunny
import requests
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

games = ["animal-crossing", "wild-world", "new-leaf", "new-horizons"]
weathers = ["sunny", "snowing", "raining"]
times = [str(i % 12 + 1) + "am" if i // 12 == 0 else str(i % 12 + 1) + "pm" for i in range(24)]
hourly_url = "https://acmusicext.com/static"

# all hourly stuff
for game in games:
    if not os.path.exists(game):
        os.makedirs(game)
    for weather in weathers:
        for time in times:
            r = requests.get(f"{hourly_url}/{game}/{weather}/{time}.ogg")
            with open(f"{DIR_PATH}/../{game}/{time}_{weather}.ogg", "wb") as f:
                f.write(r.content)

# kk sstuff
kksongs = [
    "AC - Aloha K.K.",
    "AC - Cafe K.K.",
    "AC - Comrade K.K.",
    "AC - DJ K.K.",
    "AC - Go K.K. Rider!",
    "AC - I Love You",
    "AC - Imperial K.K.",
    "AC - K.K. Aria",
    "AC - K.K. Ballad",
    "AC - K.K. Blues",
    "AC - K.K. Bossa",
    "AC - K.K. Calypso",
    "AC - K.K. Casbah",
    "AC - K.K. Chorale",
    "AC - K.K. Condor",
    "AC - K.K. Country",
    "AC - K.K. Cruisin'",
    "AC - K.K. D & B",
    "AC - K.K. Dirge",
    "AC - K.K. Etude",
    "AC - K.K. Faire",
    "AC - K.K. Folk",
    "AC - K.K. Fusion",
    "AC - K.K. Gumbo",
    "AC - K.K. Jazz",
    "AC - K.K. Lament",
    "AC - K.K. Love Song",
    "AC - K.K. Lullaby",
    "AC - K.K. Mambo",
    "AC - K.K. March",
    "AC - K.K. Parade",
    "AC - K.K. Ragtime",
    "AC - K.K. Reggae",
    "AC - K.K. Rock",
    "AC - K.K. Safari",
    "AC - K.K. Salsa",
    "AC - K.K. Samba",
    "AC - K.K. Ska",
    "AC - K.K. Song",
    "AC - K.K. Soul",
    "AC - K.K. Steppe",
    "AC - K.K. Swing",
    "AC - K.K. Tango",
    "AC - K.K. Technopop",
    "AC - K.K. Waltz",
    "AC - K.K. Western",
    "AC - Lucky K.K.",
    "AC - Mr. K.K.",
    "AC - Only Me",
    "AC - Rockin' K.K.",
    "AC - Senor K.K.",
    "AC - Soulful K.K.",
    "AC - Surfin' K.K.",
    "AC - The K. Funk",
    "AC - Two Days Ago",
    "CF - Agent K.K.",
    "CF - Forest Life",
    "CF - K.K. Dixie",
    "CF - K.K. House",
    "CF - K.K. Marathon",
    "CF - K.K. Metal",
    "CF - K.K. Rally",
    "CF - K.K. Rockabilly",
    "CF - K.K. Sonata",
    "CF - King K.K.",
    "CF - Marine Song 2001",
    "CF - Mountain Song",
    "CF - My Place",
    "CF - Neapolitan",
    "CF - Pondering",
    "CF - Spring Blossoms",
    "CF - Stale Cupcakes",
    "CF - Steep Hill",
    "CF - To the Edge",
    "CF - Wandering",
    "NL - Bubblegum K.K.",
    "NL - Hypno K.K.",
    "NL - K.K. Adventure",
    "NL - K.K. Bazaar",
    "NL - K.K. Birthday",
    "NL - K.K. Disco",
    "NL - K.K. Flamenco",
    "NL - K.K. Groove",
    "NL - K.K. Island",
    "NL - K.K. Jongara",
    "NL - K.K. Milonga",
    "NL - K.K. Moody",
    "NL - K.K. Oasis",
    "NL - K.K. Stroll",
    "NL - K.K. Synth",
    "NL - Space K.K.",
    "NH - Animal City",
    "NH - Drivin'",
    "NH - Farewell",
    "NH - Welcome Horizons",
]
styles = ["aircheck", "live"]
kk_url = "https://acmusicext.com/static/kk"

for style in styles:
    if not os.path.exists(style):
        os.makedirs(style)
    for song in kksongs:
        r = requests.get(f"{kk_url}/{style}/{song}.ogg")
        with open(f"{DIR_PATH}/../{style}/{song}.ogg", "wb") as f:
            f.write(r.content)

# iMessage Lyric Bot

Quick little bot that runs on a MacOS based system and spams your friend of choice with the top song of any artist you'd like. Serves them right for not enjoying your favorite artist.
<br><br>See it in action:
- Terminal: [YouTube](https://youtu.be/2JguwIQvIOQ)
- Phone: [YouTube](https://youtu.be/sgbRZY1NJew)

<br>

## How it works

- For this to work, it needs permission access to run system commands, since it uses the iMessage app.
- You'll be asked what number and what artist, and then simply sit back and watch as they end up blocking you.

<br>

## How to use

- NOTE: this only works on MacOS systems and on phone numbers associated with iMessage.
- This program uses the Genius API to find information on the artist of your choice. You will need an API key from their website (which is really not that hard). You can do so [here](https://docs.genius.com/#/getting-started-h1). This key would be placed near the top of ```program.py```
- I have also used Beautiful Soup, a python library that makes web scraping really easy. If you don't have it installed, you can check it out [here](https://pypi.org/project/beautifulsoup4/).
- And of course, the python ```requests``` library which allows me to make HTTP requests in python. Check it out [here](https://pypi.org/project/requests/).
- Once you have all of this set up, simply open up the directory for this repository, and type in ``` python3 prank.py``` in your terminal.

<br>

## Customer Reviews
This program guarantees atleast a 65% chance of getting blocked, and a 100% chance of your friends hating you
<br>
<br>
<br>
![screenshot of my friends hating me pt. 1](https://github.com/shashanklal01/iMessage-Lyric-Bot/blob/main/a.PNG)

![screenshot of my friends hating me pt. 2](https://github.com/shashanklal01/iMessage-Lyric-Bot/blob/main/IMG_5716.PNG)

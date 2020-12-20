# Make HTTP requests
import requests
# Scrape data from an HTML document
from bs4 import BeautifulSoup
# I/O
import os
# Search and manipulate strings
import re
# library to send imessages using mac
from py_imessage import imessage

import time

GENIUS_API_TOKEN = 'i removed mine bc this is a public repo lol'

# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []

    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)

        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)

        if (len(songs) == song_cap):
            break
        else:
            page += 1
    return songs


# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
    cur = requests.get(url)
    html = BeautifulSoup(cur.text, 'html.parser')
    scraped = html.find('div', class_='lyrics').get_text()
    # remove identifiers like chorus, verse, etc
    scraped = re.sub(r'[\(\[].*?[\)\]]', '', scraped)
    # remove empty lines
    scraped = os.linesep.join([x for x in scraped.splitlines() if x])
    return scraped


# scrapes lyrics using above functions and then writes to local file
def write_lyrics_to_file(artist_name, song_count):
    curFile = open('lyrics.txt', 'w')
    url = request_song_url(artist_name, song_count)
    scraped = scrape_song_lyrics(url[0])
    curFile.write(scraped)
    curFile.close()


# opens up the locally stored file with the scraped lyrics
# and then stores all the words in one huge array and returns
def get_words():
    allWords = []
    with open('lyrics.txt', 'r') as cur:
        text = cur.readlines()
        for line in text:
            words = line.split()
            for x in words:
                allWords.append(x)
    return allWords


# runs an applescript that runs a command using my mac applications
def send_message(phone_number, message):
    os.system('osascript script.scpt {} "{}"'.format(phone_number, message))


# main
if __name__ == '__main__':
    # put your phone number into the string!
    # if your number is (123)456-7890, the next line should look like this: phone_number = '1234567890'
    phone_number = input("what is your friend's number? ")
    artist = input("which artist do you want to spam your friends with? ")
    print("\n------ wise choice, let the trouble begin ------\n")
    write_lyrics_to_file(artist, 1)
    words = get_words()
    for word in words:
        send_message(phone_number, word)

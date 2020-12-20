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

GENIUS_API_TOKEN = 'wvvaQdHGDXnawyXlygwjDpGhq3g69ngO354a2PNwT_3EigNXi4tjtPxm7irTpI--'

# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
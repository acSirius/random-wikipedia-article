import requests
import os
import json 
import random 
import string
import webbrowser
from bs4 import BeautifulSoup

words = json.loads(open('common_words.json').read())

def random_word():
    return random.choice(words)

word = random_word()
URL = f'https://en.wikipedia.org/wiki/{word}'
#URL = 'https://en.wikipedia.org/wiki/lsafdj1234'

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')

not_found_sintaxs = soup.findAll('b')
print(URL)

if not_found_sintaxs[1].get_text() != 'Wikipedia does not have an article with this exact name.':
    word = random_word()
    URL = f'https://en.wikipedia.org/wiki/{word}'
    webbrowser.open(URL)
else:
    webbrowser.open(URL)

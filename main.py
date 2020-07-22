import os
import json 
import requests
import random 
import string
import webbrowser

words = json.loads(open('common_words.json').read())

def random_word():
    return random.choice(words)

word = random_word()
URL = f'https://en.wikipedia.org/wiki/{word}'

webbrowser.open(URL)





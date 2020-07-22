# random-wikipedia-article
Script opens a random wikipedia article.

# Description
Python will read a json file containing thousands of english words, a random word will be chosen and then you'll be redirected to that words wikipedia page. 

# Future updates
Some words don't have a wikipedia article on them, before redirecting to the page check if it has any contents in it. 
This will be done using bs4, if a wikipedia page doesnt exist this message will show up "Wikipedia does not have an article with this exact name."
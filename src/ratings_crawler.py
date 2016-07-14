import requests
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import wordnet as wn

meaningless_words = ['this', 'that', 'very', 'just', 'like', 'with', 'than', 'then', 'from', 'more', 'many',
                     'film', 'really', 'it\'s', 'will', 'what', 'quite', 'when', 'much', 'some', 'most', 'there',
                     'their', 'should', 'doesn\'t', 'have', 'movie', 'about', 'there\'s', 'great', 'good', 'well',
                     'enough', 'best', 'still', 'another', 'little']
adjectives = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}


def split_line(text):
    words = text.split()

    for word in words:

        for char in '.():!"?,-/':
            word = word.replace(char, '')
        if len(word) > 6 and word.lower() not in meaningless_words and word.lower() not in movie:
            split_words.append(str(word))

max_pages = 1
page = 1

movie = input('Which movie would you like information for? ')
movie_title = movie.lower().replace(' ', '_')
print('Searching...')

reviews = []
split_words = []
adjective_words = []
while page <= max_pages:

    base_url = 'https://www.rottentomatoes.com/m/'
    if page == 1:
        full_ratings_url = base_url + movie_title + '/reviews/?type=user'
    else:
        full_ratings_url = base_url + movie_title + '/reviews/?page=' + str(page) + '&type=user&sort='
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}
    source_code = requests.get(full_ratings_url, headers=user_agent)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    for item in soup.findAll('div', {'class': 'user_review'}):
        reviews.append(item.text)
    page += 1

    for x in range(0, len(reviews)):
        split_line(reviews[x])

for w in split_words:
    if w in adjectives:
        adjective_words.append(w)

print(len(adjective_words))
counter = Counter(adjective_words)
print(counter)

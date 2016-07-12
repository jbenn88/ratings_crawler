import requests
from bs4 import BeautifulSoup


#def ratings_crawler(max_pages):
   # page = 1
   # while page < max_pages:
movie = input('Which movie would you like information for? ')
movie_title = movie.lower().replace(' ', '_')

base_url = 'https://www.rottentomatoes.com/m/'
full_ratings_url = base_url + movie_title + '/reviews/?type=user'

user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}
source_code = requests.get(full_ratings_url, headers=user_agent)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
#print(soup)

for item in soup.findAll('div', {'class' : 'user_review'}):
    print(item.text)
    print()
"""
date_today = date.today()
print()
print("Headlines for " + calendar.day_name[date_today.weekday()] + " {:%B %d, %Y}".format(date_today) + ":\n")

url = 'https://www.rottentomatoes.com/'
user_agent = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
source_code = requests.get(url, headers=user_agent)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

"""
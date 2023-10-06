#!/usr/bin/env python

#scrape mp forums searching for titles containing "searches" string(s)
#https://www.geeksforgeeks.org/python-web-scraping-tutorial/
#https://realpython.com/beautiful-soup-web-scraper-python/#:~:text=Beautiful%20Soup%20is%20a%20Python,web%20page%20using%20developer%20tools.



import requests
from bs4 import BeautifulSoup


print("Hello World")


base = 'https://www.mountainproject.com/forum/103989416/for-sale-for-free-want-to-buy?page={}'

subcat = 'topic'

searches=['highli','staic','van','bus']


page = 1
stopAt = 2000

while page <= stopAt:
  url = base.format(page)
  print('searching page {}...'.format(page),flush=True)

  r = requests.get(url)
  if r.status_code == 200:

    soup = BeautifulSoup(r.content, 'html.parser')
    # find all the anchor tags with "href"  
    for link in soup.find_all('a'):
      h = link.get('href')
      topic = str(h)
      if subcat in topic:
        #print(topic)
        for search in searches:
          if search in topic:
            print("............")
            print('\n\nFound string {}'.format(search),flush=True)
            print(topic,flush=True)
            print("............")


  else:
    print("error found")
    print(r) 
    break


  page = page +1










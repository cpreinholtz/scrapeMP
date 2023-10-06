# ScrapeMP
Licensed under GNU GPLv3 

## design
Uses HTTP requests and beautiful soup to scrape mountain project forum titles.
Currently only works with strings one word or less

## dependencies
requests and beautiful soup:
> pip install requests
> pip install bs4

## resources
https://www.geeksforgeeks.org/python-web-scraping-tutorial/

https://realpython.com/beautiful-soup-web-scraper-python/#:~:text=Beautiful%20Soup%20is%20a%20Python,web%20page%20using%20developer%20tools.

## todo
- dump output into a better format not just print it,  perhaps just a csv or even a database???
- make multi word searches works
- make searches smarter order / caps agnostic etc
- add another step to calculate distance, price, sold/ not sold etc
- make this into a process that can run in the background / at startup
- email you alerts for new items

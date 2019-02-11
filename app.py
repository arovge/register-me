from bs4 import BeautifulSoup
import requests

webpage = 'https://austinrovge.me'

# get the webpage
page = requests.get(webpage)
print(page.content)

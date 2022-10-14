import requests
from bs4 import BeautifulSoup

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text)

metas = soup.find_all('meta')

print([meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description'])
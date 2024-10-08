import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/70.0.3538.110 Safari/537.36', 'Accept-Language':'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1'}

response = requests.get('https://www.imdb.com/chart/top/', headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

data = json.loads(soup.find('script', {'type':"application/ld+json"}).text)

print(len(data['itemListElement']))
name=[]
description=[]
rating=[]
rating_count=[]
genre=[]
duration=[]
for item in data['itemListElement'][:250]:
    name.append(item['item']['name'])
    description.append(item['item']['description'])
    rating.append(item['item']['aggregateRating']['ratingValue'])
    rating_count.append(item['item']['aggregateRating']['ratingCount'])
    genre.append(item['item']['genre'])
    s=item['item']['duration']
    duration.append(s[2:])
df=pd.DataFrame({'name':name,'rating':rating,'genre':genre,'rating_count':rating_count,'duration':duration,'description':description})
print(df.head(5))
df.to_csv("movies.csv")



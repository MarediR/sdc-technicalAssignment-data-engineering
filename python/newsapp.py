from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import mysql.connector

newsapi = NewsApiClient(api_key='57d708bd6e3a46af9761f57ddf85b9d4')

df = newsapi.get_everything(q='Coco Chanel', language='en', from_param='2022-06-24', to='2022-07-01')

data1 = newsapi.get_top_headlines(q='ukraine', language='en')
topheadlines = data1['articles']
df1 = pd.DataFrame(topheadlines)
print(df1)


data2 = newsapi.get_everything(q='ukraine', language='en', from_param='2022-06-25', to='2022-07-07')
articles = data2['articles']
df2 = pd.DataFrame(articles)
print(df2)



data3 = newsapi.get_sources()
sources = data3['sources']
df3 = pd.DataFrame(sources)
print(df3)

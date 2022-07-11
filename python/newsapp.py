from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
import mysql.connector
import sqlalchemy as sq 


newsapi = NewsApiClient(api_key='57d708bd6e3a46af9761f57ddf85b9d4')

con = sq.create_engine("mysql+pymysql://root:root@localhost:3306/news")

#Create top headlines dataframe
data1 = newsapi.get_top_headlines(q='soccer', language='en')
topheadlines = data1['articles']
df1 = pd.DataFrame(topheadlines)
df1.set_axis(['source_id', 'author', 'title', 'source_description','source_url', 'url_to_image', 'publishedAt', 'content'  ], axis='columns', inplace=True)
df1 = df1.filter(['author', 'title', 'source_description','source_url', 'url_to_image', 'publishedAt', 'content'],axis=1)
print(df1)

#Write out top headlines data to mysqlsql database
df1.to_sql("toparticles",con,if_exists="append", index=False)
print("Data written successfuly to toparticles table")

#create get everything dataframe
data2 = newsapi.get_everything(q='ukraine', language='en', from_param='2022-06-30', to='2022-07-11')
articles = data2['articles']
df2 = pd.DataFrame(articles)
df2.set_axis(['source_id', 'author', 'title', 'source_description','source_url', 'url_to_image', 'publishedAt', 'content'  ], axis='columns', inplace=True)
df2 = df2.filter(['author', 'title', 'source_description','source_url', 'url_to_image', 'publishedAt', 'content'],axis=1)
print(df2)


#Write out top headlines data to mysql database
df2.to_sql("articles",con,if_exists="append", index=False)
print("Data written successfully to articles table")

data3 = newsapi.get_sources()
sources = data3['sources']
df3 = pd.DataFrame(sources)
df3.set_axis(['source_id', 'source_name', 'source_description', 'source_url', 'category', 'source_language', 'country'  ], axis='columns', inplace=True)
print(df3)

#Write out sources data to mysql database
df3.to_sql("sources",con,if_exists="append", index=False)
print("Data written successfuly to sources table")

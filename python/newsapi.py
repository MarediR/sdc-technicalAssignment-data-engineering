from newsapi import NewsApiClient
import datetime as dt
import pandas as pd

newsapi = NewsApiClient(api_key='57d708bd6e3a46af9761f57ddf85b9d4')

df = newsapi.get_everything(q='Coco Chanel', language='en', from_param='2022-06-24', to='2022-07-01',country='eu')

type(df)
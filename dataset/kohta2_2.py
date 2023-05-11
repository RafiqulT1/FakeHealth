import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import stweet as st

def try_tweet_by_id_scrap(tweet_id):
    id_task = st.TweetsByIdTask(tweet_id)
    output_json = st.JsonLineFileRawOutput('output_raw_id.jl')
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(tweets_by_id_task=id_task,
                        raw_data_outputs=[output_print, output_json]).run()
    

df_reviews = pd.read_json('reviews\HealthStory.json', orient='records')
df_engagements = pd.read_json('engagements\HealthStory.json', orient='columns')


ratings = []
for rating in df_reviews["rating"]:
    ratings.append(rating)

ids = []
for aidi in df_reviews["news_id"]:
    ids.append(aidi)

kaikki = []
for i in range(len(ratings)):
    kaikki.append((ids[i], ratings[i]))

# TODO: list of untrusted news
untrusted_news = []
# TODO: list of trusted news
trusted_news = []

# trusted_news = kaikki luotetut uutiset
# untrusted_news = kaikki epäluotetut uutiset
for i in kaikki:
    if i[1] < 3:
        untrusted_news.append(i[0])
    else:
        trusted_news.append(i[0])

print(trusted_news)

for news in trusted_news:
    print(news)
    tweet_id = df_engagements[news]["tweets"][0]
    print(tweet_id)

    try_tweet_by_id_scrap(tweet_id)

    tweet_df = pd.read_json('output_raw_id.jl', lines=True, orient='columns')
    break
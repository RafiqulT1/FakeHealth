import pandas as pd
import json
import os
import twitter_api

# followers_folder = "user_network\\user_followers"
# following_folder = "user_network\\user_following"
# follower_user_ids = os.listdir(followers_folder)
# following_user_ids = os.listdir(following_folder)


df = pd.read_json('reviews\HealthStory.json', orient='records')
df2 = pd.read_json('engagements\HealthStory.json', orient='columns')


ratings = []
for rating in df["rating"]:
    ratings.append(rating)

ids = []
for aidi in df["news_id"]:
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

# print(f"Luotettuja yhteensä: {len(trusted_news)}")
# print(f"Epäuotettuja yhteensä: {len(untrusted_news)}")

# TODO: assing an id per every trusted and untrusted news and make tuples out of everyone.
trusted_tuples = []
untrusted_tuples = []

# assing a single user id for each news in fake and real dataset
for news in trusted_news:
    if df2[news]['tweets'] == []:
        continue
    else:
        user_id = df2[news]['tweets'][0]
        trusted_tuples.append([news, user_id])
for news in untrusted_news:
    if df2[news]['tweets'] == []:
        continue
    else:
        user_id = df2[news]['tweets'][0]
        untrusted_tuples.append([news, user_id])


# make the Fake tweets file
# for i in range(len(untrusted_tuples)):
#     twitter_api.try_tweet_by_id_scrap(untrusted_tuples[i][1], "Fake_output_raw_id.jl")

# make the Real tweets file
# for i in range(len(trusted_tuples)):
#     twitter_api.try_tweet_by_id_scrap(trusted_tuples[i][1], "Real_output_raw_id.jl")

# put followers and followees to their lists
trusted_followers = []
trusted_followees = []
untrusted_followers = []
untrusted_followees = []

things = []
with open('Fake_output_raw_id.jl', 'r') as file:
    for line in file:
        things = line.split(', ')
        for thing in things:
            if '"followers_count":' in thing:
                untrusted_followers.append(int(thing[18:]))
            if '"friends_count":' in thing:
                untrusted_followees.append(int(thing[16:]))
                break
        things = []

things = []
with open('Real_output_raw_id.jl', 'r') as file:
    for line in file:
        things = line.split(', ')
        for thing in things:
            if '"followers_count":' in thing:
                trusted_followers.append(int(thing[18:]))
            if '"friends_count":' in thing:
                trusted_followees.append(int(thing[16:]))
                break
        things = []

print(f"length of trusted tuples: {len(trusted_tuples)}")
print(f"length of trusted followers: {len(trusted_followers)}")
print(f"length of trusted followees: {len(trusted_followees)}")
print()
print(f"length of untrusted tuples: {len(untrusted_tuples)}")
print(f"length of untrusted followers: {len(untrusted_followers)}")
print(f"length of untrusted followees: {len(untrusted_followees)}")


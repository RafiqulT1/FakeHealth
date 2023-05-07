import pandas as pd
import json
import os

followers_folder = "user_network\\user_followers"
following_folder = "user_network\\user_following"
follower_user_ids = os.listdir(followers_folder)
following_user_ids = os.listdir(following_folder)


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

print(f"Luotettuja yhteensä: {len(trusted_news)}")
print(f"Epäuotettuja yhteensä: {len(untrusted_news)}")

# TODO: assing an id per every trusted and untrusted news and make tuples out of everyone.
trusted_tuples = []
untrusted_tuples = []

# print(user_ids[3])
for i, news in enumerate(trusted_news):
    trusted_tuples.append((news, follower_user_ids[i]))
for i, news in enumerate(untrusted_news):
    untrusted_tuples.append((news, follower_user_ids[i + 1217]))


# TODO: retrieve the number of followers and followees for each id in trusted and untrusted
trusted_information = []
untrusted_information = []

# fill the trusted information list
for i in range(len(trusted_news)):
    # make a dataframe for the followers and following json files
    followers_df = pd.read_json(f'user_network\\user_followers\\{follower_user_ids[i]}', orient='columns')
    following_df = pd.read_json(f'user_network\\user_following\\{following_user_ids[i]}', orient='columns')
    # append the data to the list
    trusted_information.append((trusted_tuples[i][0], trusted_tuples[i][1][:-5], followers_df['ids'].count(), following_df['ids'].count()))
# fill the untrusted information list
for i in range(len(untrusted_news)):
    followers_df = pd.read_json(f'user_network\\user_followers\\{follower_user_ids[i]}', orient='columns')
    following_df = pd.read_json(f'user_network\\user_following\\{following_user_ids[i]}', orient='columns')
    # append the data to the list
    untrusted_information.append((untrusted_tuples[i][0], untrusted_tuples[i][1][:-5], followers_df['ids'].count(), following_df['ids'].count()))


for info in trusted_information:
    print(info)
print("================================================")
for info in untrusted_information:
    print(info)

print(f"trusted_information pituus: {len(trusted_information)}")
print(f"untrusted_information pituus: {len(untrusted_information)}")

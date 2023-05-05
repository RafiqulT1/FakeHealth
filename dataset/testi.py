import pandas as pd
import json

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

untrusted = []
trusted = []

for i in kaikki:
    if i[1] < 3:
        untrusted.append(i[0])
    else:
        trusted.append(i[0])

print(f"Luotettuja yhteensä: {len(trusted)}")
print(f"Epäuotettuja yhteensä: {len(untrusted)}")


# TODO: average tweets per trusted
trusted_tweets = []
for user in trusted:
    count = 0
    for tweet in df2[user]["tweets"]:
        count += 1
    trusted_tweets.append(count)
print(f"Average tweets per trusted: \t{sum(trusted_tweets) / len(trusted_tweets)}")


# TODO: average retweets per trusted
trusted_retweets = []
for user in trusted:
    count = 0
    for retweet in df2[user]["retweets"]:
        count += 1
    trusted_retweets.append(count)
print(f"Average retweets per trusted: \t{sum(trusted_retweets) / len(trusted_retweets)}")

# TODO: average replies per trusted
trusted_replies = []
for user in trusted:
    count = 0
    for reply in df2[user]["replies"]:
        count += 1
    trusted_replies.append(count)
print(f"Average replies per trusted: \t{sum(trusted_replies) / len(trusted_replies)}")

# TODO: average tweets per untrusted
untrusted_tweets = []
for user in untrusted:
    count = 0
    for tweet in df2[user]["tweets"]:
        count += 1
    untrusted_tweets.append(count)
print(f"Average tweets per untrusted: \t{sum(untrusted_tweets) / len(untrusted_tweets)}")

# TODO: average retweets per untrusted
untrusted_retweets = []
for user in untrusted:
    count = 0
    for retweet in df2[user]["retweets"]:
        count += 1
    untrusted_retweets.append(count)
print(f"Average retweets per untrusted: {sum(untrusted_retweets) / len(untrusted_retweets)}")

# TODO: average replies per untrusted
untrusted_replies = []
for user in untrusted:
    count = 0
    for reply in df2[user]["replies"]:
        count += 1
    untrusted_replies.append(count)
print(f"Average replies per untrusted: \t{sum(untrusted_replies) / len(untrusted_replies)}")


trusted_zipped = list(zip(trusted, trusted_tweets, trusted_retweets, trusted_replies))
untrusted_zipped = list(zip(untrusted, untrusted_tweets, untrusted_retweets, untrusted_replies))
trusted_df = pd.DataFrame(trusted_zipped, columns=["trusted", "trusted_tweets", "trusted_retweets", "trusted_replies"])
untrusted_df = pd.DataFrame(untrusted_zipped, columns=["untrusted", "untrusted_tweets", "untrusted_retweets", "untrusted_replies"])
print(trusted_df)
print(untrusted_df)

trusted_df_std = trusted_df.std(numeric_only=True)
trusted_df_kurtosis = trusted_df.kurtosis(numeric_only=True)
trusted_df_skew = trusted_df.skew(numeric_only=True)
untrusted_df_std = untrusted_df.std(numeric_only=True)
untrusted_df_kurtosis = untrusted_df.kurtosis(numeric_only=True)
untrusted_df_skew = untrusted_df.skew(numeric_only=True)
print(f"Untrusted std:\n{untrusted_df_std}")
print()
print(f"Trusted std:\n{trusted_df_std}")
print()
print(f"Untrusted kurtosis:\n{untrusted_df_kurtosis}")
print()
print(f"Trusted kurtosis:\n{trusted_df_kurtosis}")
print()
print(f"Untrusted skewness:\n{untrusted_df_skew}")
print()
print(f"Trusted skewness:\n{trusted_df_skew}")
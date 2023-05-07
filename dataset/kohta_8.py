import pandas as pd
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_json('reviews\HealthStory.json', orient='records')

# place the descriptions to the list
descriptions = []
for desc in df["description"]:
    descriptions.append(desc)

ratings = []
for rating in df["rating"]:
    ratings.append(rating)

ids = []
for aidi in df["news_id"]:
    ids.append(aidi)

kaikki = []
for i in range(len(ratings)):
    kaikki.append((ids[i], ratings[i], descriptions[i]))

untrusted_news_and_descriptions = []
trusted_news_and_descriptions = []

for i in kaikki:
    if i[1] < 3:
        untrusted_news_and_descriptions.append((i[0], i[2]))
    else:
        trusted_news_and_descriptions.append((i[0], i[2]))

# initialize the analyzer
analyzer = SentimentIntensityAnalyzer()

# real dataset
pos_summa = 0
neg_summa = 0
neu_summa = 0
for desc in trusted_news_and_descriptions:
    vs = analyzer.polarity_scores(desc[1])
    pos_summa += vs['pos']
    neg_summa += vs['neg']
    neu_summa += vs['neu']
# fake dataset
pos_summa = 0
neg_summa = 0
neu_summa = 0
for desc in untrusted_news_and_descriptions:
    vs = analyzer.polarity_scores(desc[1])
    pos_summa += vs['pos']
    neg_summa += vs['neg']
    neu_summa += vs['neu']
    # print("{:-<65} {}".format(desc[1], str(vs)))
    # print(str(vs))
print(f"Real dataset average positivity: {pos_summa / len(trusted_news_and_descriptions)}")
print(f"Real dataset average negativity: {neg_summa / len(trusted_news_and_descriptions)}")
print(f"Real dataset average neutrality: {neu_summa / len(trusted_news_and_descriptions)}")
print()
print(f"Fake dataset average positivity: {pos_summa / len(untrusted_news_and_descriptions)}")
print(f"Fake dataset average negativity: {neg_summa / len(untrusted_news_and_descriptions)}")
print(f"Fake dataset average neutrality: {neu_summa / len(untrusted_news_and_descriptions)}")

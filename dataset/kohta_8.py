import pandas as pd
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_json('reviews\HealthStory.json', orient='records')

# place the descriptions to the list
descriptions = []
for desc in df["original_title"]:
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
#
trusted_values =  []
untrusted_values = []
# real dataset
pos_summa = 0
neg_summa = 0
neu_summa = 0
for desc in trusted_news_and_descriptions:
    vs = analyzer.polarity_scores(desc[1])
    pos_summa += vs['pos']
    neg_summa += vs['neg']
    neu_summa += vs['neu']
    trusted_values.append({"pos":vs['pos'],
                           "neg":vs['neg'],
                           "neu":vs['neu'],
                           "label":desc})
# fake dataset
pos_summa = 0
neg_summa = 0
neu_summa = 0
for desc in untrusted_news_and_descriptions:
    vs = analyzer.polarity_scores(desc[1])
    pos_summa += vs['pos']
    neg_summa += vs['neg']
    neu_summa += vs['neu']
    untrusted_values.append({"pos":vs['pos'],
                           "neg":vs['neg'],
                           "neu":vs['neu'],
                           "label":desc})
    # print("{:-<65} {}".format(desc[1], str(vs)))
    # print(str(vs))
print(f"Real dataset average positivity: {pos_summa / len(trusted_news_and_descriptions)}")
print(f"Real dataset average negativity: {neg_summa / len(trusted_news_and_descriptions)}")
print(f"Real dataset average neutrality: {neu_summa / len(trusted_news_and_descriptions)}")
print()
print(f"Fake dataset average positivity: {pos_summa / len(untrusted_news_and_descriptions)}")
print(f"Fake dataset average negativity: {neg_summa / len(untrusted_news_and_descriptions)}")
print(f"Fake dataset average neutrality: {neu_summa / len(untrusted_news_and_descriptions)}")

# # #
# Drawing ternary plot
# Code taken from https://plotly.com/python/ternary-plots/ ; Ternary scatter plot with Plotly Graph Objects

import plotly.graph_objects as go

# rawData uses format:
#  [
#     {'a':75,'b':25,'c':0,'label':'point 1'}, 
# ]

# Change rawData to untrusted_values to plot untrusted news.
rawData = trusted_values

def makeAxis(title, tickangle):
    return {
      'title': title,
      'titlefont': { 'size': 20 },
      'tickangle': tickangle,
      'tickfont': { 'size': 15 },
      'tickcolor': 'rgba(0,0,0,0)',
      'ticklen': 5,
      'showline': True,
      'showgrid': True
    }

fig = go.Figure(go.Scatterternary({
    'mode': 'markers',
    'a': [i for i in map(lambda x: x['pos'], rawData)],
    'b': [i for i in map(lambda x: x['neg'], rawData)],
    'c': [i for i in map(lambda x: x['neu'], rawData)],
    'text': [i for i in map(lambda x: x['label'], rawData)],
    'marker': {
        'symbol': 100,
        'color': '#DB7365',
        'size': 14,
        'line': { 'width': 2 }
    }
}))

fig.update_layout({
    'ternary': {
        'sum': 1,
        'aaxis': makeAxis('Positive', 0),
        'baxis': makeAxis('<br>Negative', 45),
        'caxis': makeAxis('<br>Neutral', -45)
    },
    'annotations': [{
      'showarrow': False,
      'text': 'Sentiment of trusted news',
        'x': 0.5,
        'y': 1.3,
        'font': { 'size': 15 }
    }]
})

fig.show()

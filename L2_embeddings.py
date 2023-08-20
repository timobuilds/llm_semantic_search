import os
import cohere
import umap
import utils
import pandas as pd
import altair as alt

# read local .env file
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

#create a cohere client using api key
co = cohere.Client(os.environ['COHERE_API_KEY'])

import pandas as pd

#word embeddings - consider small dataset of three words

three_words = pd.DataFrame({'text':
  [
      'joy',
      'happiness',
      'potato'
  ]})

#create embeddings with cohere embedd function
three_words_emb = co.embed(texts=list(three_words['text']),
                           model='embed-english-v2.0').embeddings

#explore each vector embedding
word_1 = three_words_emb[0]
word_2 = three_words_emb[1]
word_3 = three_words_emb[2]

#chaec a vector embedding
word_1[:10]

#sentance embeddings

sentences = pd.DataFrame({'text':
  [
   'Where is the world cup?',
   'The world cup is in Qatar',
   'What color is the sky?',
   'The sky is blue',
   'Where does the bear live?',
   'The bear lives in the the woods',
   'What is an apple?',
   'An apple is a fruit',
  ]})

sentences

#create embeddings for three sentances
emb = co.embed(texts=list(sentences['text']),
               model='embed-english-v2.0').embeddings

# Explore the 10 first entries of the embeddings of the 3 sentences:
for e in emb:
    print(e[:3])

len(emb[0])

from utils import umap_plot

chart = umap_plot(sentences, emb)

chart.interactive()

#Ceate embeddings for some articles from Wikipedia
wiki_articles = pd.read_pickle('wikipedia.pkl')
wiki_articles

import numpy as np
from utils import umap_plot_big

articles = wiki_articles[['title', 'text']]
embeds = np.array([d for d in wiki_articles['emb']])

chart = umap_plot_big(articles, embeds)
chart.interactive()



import os
import weaviate
import utils
import cohere

# read local .env file
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# Import weaviate to access Wikipedia db
auth_config = weaviate.auth.AuthApiKey(api_key=os.environ['WEAVIATE_API_KEY'])


# Conect this client to a public database from Wikipedia. Each row is a passage from 10 languages in wikipedia.
client = weaviate.Client(
    url="https://cohere-demo.weaviate.network/",
    auth_client_secret=auth_config,
    additional_headers={
        "X-Cohere-Api-Key": os.environ['COHERE_API_KEY'],
    }
)


#dense retrieval
from utils import dense_retrieval

query = "What is the capital of Canada?"

dense_retrieval_results = dense_retrieval(query, client)

from utils import print_result

print_result(dense_retrieval_results)


#improving keyword search with rerank
from utils import keyword_search

query_1 = "What is the capital of Canada?"


results = keyword_search(query_1,
                         client,
                         properties=["text", "title", "url", "views", "lang", "_additional {distance}"],
                         num_results=3
                        )

for i, result in enumerate(results):
    print(f"i:{i}")
    print(result.get('title'))
    print(result.get('text'))


    uery_1 = "What is the capital of Canada?"
results = keyword_search(query_1,
                         client,
                         properties=["text", "title", "url", "views", "lang", "_additional {distance}"],
                         num_results=500
)

for i, result in enumerate(results):
    print(f"i:{i}")
    print(result.get('title'))
    #print(result.get('text'))

def rerank_responses(query, responses, num_responses=10):
    reranked_responses = co.rerank(
        model = 'rerank-english-v2.0',
        query = query,
        documents = responses,
        top_n = num_responses,
        )
    return reranked_responses


texts = [result.get('text') for result in results]
reranked_text = rerank_responses(query_1, texts)


for i, rerank_result in enumerate(reranked_text):
    print(f"i:{i}")
    print(f"{rerank_result}")
    print()


#improving dense retrieval with rerank

from utils import dense_retrieval

query_2 = "Who is the tallest person in history?"

results = dense_retrieval(query_2,client)

for i, result in enumerate(results):
    print(f"i:{i}")
    print(result.get('title'))
    print(result.get('text'))
    print()

texts = [result.get('text') for result in results]
reranked_text = rerank_responses(query_2, texts)

for i, rerank_result in enumerate(reranked_text):
    print(f"i:{i}")
    print(f"{rerank_result}")
    print()


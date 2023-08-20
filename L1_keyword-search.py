
import os
import weaviate

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

#Check if this local weaviate client able to connect to weaviate db
client.is_ready()

# Keyword search functionc
def keyword_search(query,
                   results_lang='en',
                   properties = ["title","url","text"],
                   num_results=3):

    where_filter = {
    "path": ["lang"],
    "operator": "Equal",
    "valueString": results_lang
    }
    
    response = (
        client.query.get("Articles", properties)
        .with_bm25(
            query=query
        )
        .with_where(where_filter)
        .with_limit(num_results)
        .do()
        )

    result = response['data']['Get']['Articles']
    return result


# Call the function
query = "What is the most viewed televised event?"
keyword_search_results = keyword_search(query)
print(keyword_search_results)

#print in a different format thats easier to read

def print_result(result):
    """Use colourful formatting"""
    for i,item in enumerate(result):
        print(f'item {i}')
        for key in item.keys():
           print (f"{key}: {item.get(key)}")
           print()
        print()
    
print_result(keyword_search_results)


#modify search options to get more results
#Other languages to try: en, de, fr, es, it, ja, ar, zh, ko, hi

properties = ["text", "title", "url", "views", "lang"]

# Call the function
query = "What is the most viewed televised event?"
keyword_search_results = keyword_search(query, results_lang='de')
print(keyword_search_results)

print_result(keyword_search_results)
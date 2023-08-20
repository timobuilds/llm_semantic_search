
# Semantic Keyword Search

## Introduction
------------

Keyword search is common method for search. But it is limiting for context-rich data sets. Incorporating large language models (LLMs) into your search can significantly enhance the user experience by allowing users to ask questions and find information in a much easier way.

Explores: 

- Basic keyword search
- Enhancing keyword search with the rerank method, which ranks the best responses by relevance with the query.
- Implementing dense retrieval through the use of embeddings, which uses the actual semantic meaning of the text to improve search results.
- Search-powered LLMs: Use a search model to to pull context from a dataset into an index of embeddings; have the LLM use this index to enrich the context of answers to your search queries


# Dependencies 
----------------------------
Install:

1. Clone the repository to your local machine.

2. Create VM and install dependencies from .yml

Using `micromamba`:
``` bash
cd llm-semantic_search
micromamba env create -f environment.yml
micromamba activate llm-deep
```

3. Create a `.env` file in the root directory of the project. Inside the file, add your OpenAI API key:

```makefile
WEAVIATE_API_KEY="your_api_key_here"
COHERE_API_KEY = "your_api_key_here"
```


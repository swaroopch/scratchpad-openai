"""
Using a vector database.

https://platform.openai.com/docs/guides/embeddings/how-can-i-retrieve-k-nearest-embedding-vectors-quickly
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# TODO: https://platform.openai.com/docs/tutorials/web-qa-embeddings
# Maybe https://developer.doordash.com/en-US/docs/welcome
# https://github.com/openai/openai-cookbook/tree/main/apps/web-crawl-q-and-a
# https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/qdrant/Getting_started_with_Qdrant_and_OpenAI.ipynb
# https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/qdrant/QA_with_Langchain_Qdrant_and_OpenAI.ipynb

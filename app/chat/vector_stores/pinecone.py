import os
from pinecone import Pinecone as pinecone

from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

pc = pinecone(api_key=os.getenv("PINECONE_API_KEY"))

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)

def build_retriever(chatargs):
    search_kwargs= {
        "filter": {"pdf_id": chatargs.pdf_id},
        "k": 3
        }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )

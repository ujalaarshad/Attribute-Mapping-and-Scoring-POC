import json
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv
import logging
import pinecone

# Load environment variables
load_dotenv()
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Set up the embedding model
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)

# Load data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Combine variations into a single string and create Document objects
documents = []

for item in data:
    combined_text = " ".join(item["variations"])  # Combine all variations into a single string
    doc_metadata = {
        "command": item["command"],
        "attributes": item["attributes"]
    }
    # Create Document object
    doc = Document(page_content=combined_text, metadata=doc_metadata)
    documents.append(doc)

print(documents)  # Optional: To check the documents before storing them in Pinecone

# Generate embeddings for the combined texts and store in Pinecone
logging.info("Generating embeddings for combined variations...")

doc_search = PineconeVectorStore.from_documents(
    documents=documents,
    index_name='attributes-poc',
    embedding=embeddings
)

logging.info("Documents and embeddings stored successfully in Pinecone")



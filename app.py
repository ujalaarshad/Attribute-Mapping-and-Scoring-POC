import streamlit as st
import logging
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Initialize embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)

# Initialize Pinecone index and the vector store
doc_search = PineconeVectorStore.from_existing_index(
    index_name='attributes-poc',
    embedding=embeddings
)

# Function to search for a query
def search_query(query, k):
    logging.info(f"Searching for query: '{query}' with top-{k} results")
    results = doc_search.similarity_search_with_score(query=query, k=k)
    
    return results

# Streamlit UI setup
st.title("Attributes Search and Scores")

# Input query
query = st.text_input("Enter your query:", "")

# Select top-k results
k = st.slider("Select number of top results to display", 1, 50, 3)

# Search button
if st.button("Search"):
    if query:
        st.subheader(f"Results for: '{query}'")
        results = search_query(query, k)
        
        # Display the results in a more readable format
        for res, score in results:
            st.markdown(f"**Command**: `{res.metadata['command']}`", unsafe_allow_html=True)
            st.markdown(f"**Attributes**: <span style='color:green'>{res.metadata['attributes']}</span>", unsafe_allow_html=True)
            st.write(f"**Score**: {score:.3f}")
            st.markdown("---")
    else:
        st.warning("Please enter a query before searching.")



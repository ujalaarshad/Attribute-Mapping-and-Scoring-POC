# README for Attribute Search Application

This repository contains a Streamlit-based web application that interacts with Pinecone for searching documents based on user queries. The application uses OpenAI's embeddings to search relevant documents and display their corresponding commands, attributes, and similarity scores.

### Project Structure:

1. **`app.py`**: This is the main Streamlit app where the user inputs a query, selects the number of top results, and presses the "Search" button to get the relevant documents.
   
   - **Key functionality**: 
     - Query input
     - Top-k results selection
     - Displaying the command in code style and attributes in a styled format
     - Displaying similarity scores
   
2. **`chunking.py`**: This script is responsible for processing the JSON data, creating `Document` objects, and storing them in Pinecone after generating embeddings. The embeddings are generated using OpenAI's model.

   - **Key functionality**:
     - Loads the JSON data
     - Combines variations into a single string and stores metadata
     - Creates documents and stores them in Pinecone

3. **`data.json`**: The JSON file containing the data to be processed and stored in Pinecone. It should have the following structure:
   ```json
   [
       {
           "command": "command1",
           "attributes": "attributes1",
           "variations": ["variation1", "variation2"]
       },
       {
           "command": "command2",
           "attributes": "attributes2",
           "variations": ["variation1", "variation2"]
       }
   ]
   ```

4. **`.env`**: Contains the necessary API keys to access Pinecone and OpenAI services. The `.env` file should have the following variables:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

---

### How to Set Up the Project:

1. **Install dependencies**:
   First, install the required libraries using `pip`. You can do this by running:
   ```bash
   pip install -r requirements.txt
   ```

   **`requirements.txt`** should include:
   ```
   streamlit
   langchain
   pinecone-client
   openai
   dotenv
   logging
   ```

2. **Set up environment variables**:
   Create a `.env` file in the root directory of the project with the following content:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

3. **Prepare your JSON data**:
   Make sure the `data.json` file is correctly formatted and located in the root directory. This file should contain the commands, attributes, and variations as described above.

4. **Run the chunking script**:
   Run the `chunking.py` script to process the JSON data, generate embeddings using OpenAI, and store the documents in Pinecone:
   ```bash
   python chunking.py
   ```

   This will load the data from `data.json`, create documents, generate embeddings, and store them in Pinecone for later retrieval.

5. **Run the Streamlit app**:
   To start the web application, run the following command:
   ```bash
   streamlit run app.py
   ```

   This will open a local Streamlit app in your browser where you can input queries, select the number of results (top-k), and see the relevant documents, commands, attributes, and similarity scores.

---

### How the Application Works:

1. **Input Query**: 
   - The user types a query in the input box on the Streamlit UI.

2. **Select Top-k Results**:
   - The user can select how many results they want to retrieve, ranging from 1 to 50, using a slider.

3. **Display Results**:
   - After the user presses the "Search" button, the application will query Pinecone using the selected top-k value.
   - For each relevant document, the application will display:
     - **Command**: The command is shown in code style.
     - **Attributes**: The attributes are displayed in green.
     - **Score**: The similarity score indicating how relevant the document is to the query.

4. **Backend**:
   - The backend uses Pinecone to store and retrieve the embeddings, and OpenAI's embedding model to generate vector embeddings for the documents.

---

### Troubleshooting:

1. **Missing Environment Variables**:
   If the `.env` file is not set up correctly, you will see errors when the application tries to access the APIs. Make sure both `PINECONE_API_KEY` and `OPENAI_API_KEY` are set.

2. **Pinecone Connection Issues**:
   Ensure that your Pinecone API key is valid and that you have access to the Pinecone service. You can test this by checking the Pinecone dashboard.

3. **Embedding Generation Errors**:
   If there are any issues with OpenAI embedding generation, check your OpenAI API key and ensure that your account is active and has sufficient usage limits.

---

### License:

This project is licensed under the MIT License. See the LICENSE file for more details.

---

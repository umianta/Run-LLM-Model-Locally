import gradio as gr

import bs4

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import WebBaseLoader

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import OllamaEmbeddings

import ollama



# Function to load, spliyt, and retrieve documents

def load_and_retrieve_docs(url):

    loader = WebBaseLoader(

        web_paths=(url,),

        bs_kwargs=dict() 

    )

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    print(text_splitter)
    splits = text_splitter.split_documents(docs)
    print(splits)
    embeddings = OllamaEmbeddings(model="mistral")
    print(f"embeddings : {embeddings}\n\n")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    print(f"vectorstore : {vectorstore} \n\n\n")
    return vectorstore.as_retriever()



# Function to format documents

def format_docs(docs):

    return "\n\n".join(doc.page_content for doc in docs)



# Function that defines the RAG chain

def rag_chain(url, question):

    retriever = load_and_retrieve_docs(url)
    print(f"retriever : {retriever}\n\n")
    retrieved_docs = retriever.invoke(question)
    print(f"retrieved_docs : {retrieved_docs} \n\n")
    formatted_context = format_docs(retrieved_docs)
    print(f"formatted_context : {formatted_context}\n\n")
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    print(f"formatted_prompt :{formatted_prompt} \n\n")
    response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': formatted_prompt}])
    print(f"model response : {response}" )
    return response['message']['content']



# Gradio interface

iface = gr.Interface(

    fn=rag_chain,

    inputs=["text", "text"],

    outputs="text",

    title="RAG Chain Question Answering",

    description="Enter a URL and a query to get answers from the RAG chain."

)



# Launch the app

iface.launch()

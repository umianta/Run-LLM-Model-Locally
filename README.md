# Run LLM Model & RAG chain Locally

You may want to run a large language model locally on your machine for many reasons. I engaged in this endeavor to gain a deeper understanding of Large Language Models (LLMs), exploring how to fine-tune and train them.

I experimented with Small LLMs and Retrieval-Augmented Generation (RAG) chain that operates locally on my machine, leveraging the computing power of the CPU. 

In the architecture of this Chatbot design, you have the flexibility to input any website URL along with a question, and the system will provide an answer. The initial phase involves downloading the content of the web page, transforming it into a vector using the Mistral Embedding model, and subsequently storing it in the Chroma Vector DB. The same process is applied to questions, converting them into embeddings. A semantic search is then conducted in the Chroma Vector DB, and the context along with the question is passed to the Mistral Large Language Model (LLM). Mistral LLM, in turn, generates well-formatted responses, which are displayed on the Chatbot UI.

The essential components I incorporated to construct and execute the LLMs model and RAG chain locally include:

1. Ollama Python library: Employed for local model execution.
2. Gradio Python library: Utilized for creating a chatbot interface.
3. Mistral LLMs model: Trained with 7 billion parameters, employed specifically for embedding and summarizing responses.
4. Chroma DB : Employed for storing vectors.
Here's the architectural diagram representing this design
![image](https://github.com/umianta/Run-LLM-Model-Locally/assets/241957/ba4f47dc-b87a-4739-9256-db933787461c)

Here is the Chatbot UI Interface  design 

![image](https://github.com/umianta/Run-LLM-Model-Locally/assets/241957/67bbe293-d8f3-464e-80d8-c1db616d2865)


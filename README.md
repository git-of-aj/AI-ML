# AI-ML
All AI
- [agentic ai vs gen ai](https://eicta.iitk.ac.in/knowledge-hub/artificial-intelligence/agentic-ai-vs-generative-ai/)
- [ Exploratory Data Analysis - EDA](https://www.geeksforgeeks.org/what-is-exploratory-data-analysis/)
### [openai labs](https://github.com/MicrosoftLearning/mslearn-openai/tree/main)
```py
how to perform - check how accurancy impacted
1. handle missing values (numpy, pandas,seaborn,matplotlib, -- kaggle kernel for example)
2. feature selection
3.
```
## RAG - Retrieval Augmented Generation
- Retrieval-Augmented Generation (RAG) combines information retrieval and text generation. It first retrieves relevant documents from a database and then uses these documents to generate more accurate and contextually informed responses, enhancing the quality of generated text by grounding it in real-world information.
- 
A real-time example of RAG is in customer support chatbots. When a user asks a specific question, the bot retrieves relevant product manuals or FAQs and uses that information to generate a precise, context-aware response, ensuring the answer is both accurate and relevant to the user's inquiry.

## Semantic Search
Semantic search improves search accuracy by understanding the meaning behind the query, rather than relying on keyword matching. It uses natural language processing (NLP) and machine learning to retrieve relevant results based on context, intent, and semantic relationships, providing more accurate and meaningful answers.
# Ai Foundry - [annoucement](https://techcommunity.microsoft.com/blog/aiplatformblog/ignite-2024-announcing-the-azure-ai-foundry-sdk/4295862)
> AI platform that includes both our Azure AI Foundry portal (formerly Azure AI Studio), and the Azure AI Foundry SDK, our unified SDK with pre-built app templates enabling developers to: 
1. Access our most popular models through a single interface 
2. Easily integrate Azure AI into their apps 
3. Evaluate, debug and improve application quality and safety across development, testing, and production environments. 

- Hub: The "big container" that holds and connects multiple projects. It's where you manage resources, security, and compute resources.
- Project: A task or AI application within the hub, where you build and fine-tune your AI models. Projects get access to resources from the hub but also have their own private storage.
- Connections: These are the bridges that let projects and hubs access other resources (like data, OpenAI models, etc.).
- Management Center: The control center where you manage everything in Azure AI Foundry.

> An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

# my project
> Azure AI Search serves as the mechanism to retrieve relevant information from your dataset, while Azure OpenAI takes that information and generates a response based on it. Together, they enable efficient, accurate, and contextually rich responses in use cases like customer support, document summarization, Q&A, and more.
RAG (Retrieval-Augmented Generation) in Action:
- Suppose you have a customer support knowledge base stored in Azure Blob Storage, indexed by Azure AI Search.
- A user asks a support query, such as "How can I reset my password?"
- Azure AI Search retrieves the relevant sections of the knowledge base that discuss password resets.
- The retrieved documents (or parts of documents) are sent to Azure OpenAI, which generates a response by synthesizing the content, perhaps answering, "To reset your password, go to the login page, click on 'Forgot Password,' and follow the instructions..."
- This response is then sent back to the user.

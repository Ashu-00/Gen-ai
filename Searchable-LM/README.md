# Searchable LM

This repository contains a Python script that allows interaction with an autonomous Large Language Model (LLM) using the Groq API, integrated with external tools such as web search via DuckDuckGo. The agent uses the ReAct (Reasoning and Action) framework to decide when to answer a query using its knowledge or perform web searches for current information. The agent can also remember previous conversations using memory.

## Features
- **LLM Integration with Groq**: The script uses Groq's LLM model (`llama-3.1-8b-instant`) to answer user queries.
- **Web Search Tool**: For queries that require up-to-date information, the agent can search the web using the DuckDuckGo search tool.
- **ReAct Agent**: Implements the ReAct framework, where the agent reasons about whether it should respond using its knowledge or perform actions such as web search.
- **Conversation Memory**: Keeps track of conversation history to ensure coherent interactions over multiple turns.

## Prerequisites

1. **Python 3.x**: Make sure you have Python 3 installed.
2. **Install dependencies**: You can install the required Python packages by running:

```bash
pip install langchain langchain_groq langchain_community duckduckgo-search
```

3. **Groq API Key**: Set up your Groq API key securely as an environment variable:

```bash
export GROQ_API_KEY="your-groq-api-key"
```

## How It Works

1. **LLM Model Initialization**: The `llama-3.1-8b-instant` model is loaded using the Groq API.
2. **Web Search Tool**: The DuckDuckGo search tool is used to retrieve real-time data from the web for queries that require the latest information.
3. **ReAct Framework**: The agent follows a decision-making process, determining whether to answer a question based on its internal knowledge or perform an external action (such as web search).
4. **Memory Management**: A conversation buffer stores the chat history, ensuring context is maintained across the conversation.

### Toolset
- **Web Search**: When the agent requires up-to-date information that it doesn't possess, it can trigger a web search using DuckDuckGo.

## Usage

1. **Set Up Your Environment**:
   - Ensure your Groq API key is set as an environment variable.
   
   ```bash
   export GROQ_API_KEY="your-groq-api-key"
   ```

2. **Run the Script**:
   - Start the interaction with the LLM by running the script:
   
   ```bash
   python app.py
   ```

3. **Interact with the Model**:
   - Type your questions and press enter to get answers from the model. If a question requires real-time data, the agent will use web search automatically.
   - To exit, type `exit`.

### Example:
```bash
Welcome to the autonomous LLM with tools!
Type 'exit' to end the conversation.

You: What is the capital of France?

AI: The capital of France is Paris.

You: Who won the last FIFA World Cup?

AI: Performing a web search...
AI: The winner of the last FIFA World Cup was Argentina (2022).
```

## Code Structure

### `interact_with_model(query: str) -> str`
This function handles interaction with the Groq LLM agent. It uses the ReAct agent to determine whether to answer directly or invoke the DuckDuckGo search tool for real-time information.

### `Tool` Object
The web search tool is defined using the `Tool` class from LangChain, providing the agent with the ability to access DuckDuckGo search results when required.

### `AgentExecutor`
The `AgentExecutor` is responsible for executing the agent's actions and managing conversation memory.

### `ConversationBufferMemory`
The agent uses `ConversationBufferMemory` to keep track of the conversation history and maintain context during multi-turn conversations.

## Error Handling
- **Iteration Limit**: If the agent hits an iteration or time limit during response generation, the script retries the query after a short delay.
- **Exceptions**: The script captures and logs errors that may occur during interactions, ensuring a smooth user experience.

## Example Folder Structure

```
/your-repo-folder
    app.py
```
---

Feel free to fork this repository, modify it, and add new tools as needed. Contributions are welcome!

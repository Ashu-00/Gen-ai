import os
from langchain import hub
from langchain_groq import ChatGroq
from langchain.agents import Tool, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
import time

# Securely get the Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq language model
model = ChatGroq(model="llama-3.1-8b-instant")

# Define tools
search_tool = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Web Search",
        func=search_tool.run,
        description="Useful for searching the web for current information. Use this when you need up-to-date facts or data that may not be in your training data. This should not be used when you can answer on your own. If the answer cannot be determined on your own, you must use this tool.",
    )
]


# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")
prompt.template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

You are an AI assistant with access to tools. You have a vast knowledge base, but for very recent information or specific facts you might need to use the Web Search tool. Use tools only when necessary, and rely on your own knowledge when possible.
If asked questions you can answer on your own, do not use web search.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be either answering on your own or one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question ( do not reply with "The final answer is ...") Do not share your thoughts until asked.
Begin!

Previous conversation history:
{chat_history}

Question: {input}
{agent_scratchpad}"""
# Initialize memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

# Create the agent without the memory parameter
agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=prompt,
)

# Create the AgentExecutor with memory handled separately
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    handle_parsing_errors=True,
)


# Function to interact with the model
def interact_with_model(query):
    response = executor.invoke({"input": query})
    while response["output"]=="Agent stopped due to iteration limit or time limit.":
        print("AI : An Error occured retrying in 5s.")
        time.sleep(4)
        response = executor.invoke({"input": query})
    return response["output"]


# Example usage
if __name__ == "__main__":
    print("Welcome to the autonomous LLM with tools!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            response = interact_with_model(user_input)
            print(f"\nAI: {response}")

            """memory.chat_memory.add_user_message(user_input)
            memory.chat_memory.add_ai_message(response)"""
        except Exception as e:
            print(f"AI: An error occurred: {e}")

# Gen-ai

Welcome to the **Gen-ai** repository! This project contains two distinct tools designed to enhance productivity through intelligent automation. One tool helps organize files in a folder based on their names, and the other enables users to interact with an autonomous Large Language Model (LLM) integrated with web search capabilities.

## Table of Contents

1. [Folder Organizer](#folder-organizer)
   - [Features](#features)
   - [Usage](#usage)
   
2. [Autonomous LLM with Tools](#autonomous-llm-with-tools)
   - [Features](#features-1)
   - [Usage](#usage-1)

---

## Folder Organizer

This tool organizes files in a specified folder into categories based on their filenames. It uses the ChatGroq language model (via Langchain) to classify files and move them into relevant subfolders.

### Features
- **File Classification**: Automatically classifies files based on their filenames into predefined categories.
- **Automatic Folder Creation**: Creates subfolders for each category if they do not exist.
- **File Organization**: Moves files to their respective categorized folders.
- **Progress Indicator**: Displays a progress bar during the organization process.

### Usage
1. Modify the `base_folder` variable in the script to point to the folder where your files are located.
2. Run the script:

   ```bash
   python folder_organizer/app.py
   ```

3. The script will classify and organize files in the specified folder.

---

## Autonomous LLM with Tools

This tool allows users to interact with an autonomous LLM using the Groq API, integrated with web search via DuckDuckGo. The agent uses a ReAct (Reasoning and Action) framework to decide when to respond using internal knowledge or perform a web search for real-time information.

### Features
- **LLM Integration**: Interacts with the `llama-3.1-8b-instant` model via Groq.
- **Web Search Tool**: Retrieves up-to-date information using DuckDuckGo.
- **ReAct Agent**: Decides when to answer queries based on internal knowledge or perform web searches.
- **Memory Management**: Keeps track of conversation history to ensure coherent responses over multiple interactions.

### Usage
1. Run the script to start the interaction:

   ```bash
   python llm_interaction/app.py
   ```

2. Type your questions and press enter. The agent will respond based on its knowledge or perform a web search if necessary.
3. To exit, type `exit`.


---

Explore the **Gen-ai** repository, fork it, and modify it as needed. Contributions and improvements are welcome!

import os
import shutil
from langchain.tools import tool
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import json
from tqdm import tqdm


# Initialize ChatGroq LLM
llm = ChatGroq(api_key=os.environ("GROQ_API"))

# Define directories based on categories
categories = ["Research Papers", "Documents", "Textbooks", "Images", "Audio Files", "Previous Year Papers", "Software", "Codes", "Others"]

# Prompt template for classifying files based on file name
prompt_template = """
Classify the following file name into one of the categories: """+ str(categories)+"""

File Name: {file_name}

Please return the result as a JSON object with the format:
{{
  "category": "Category Name"
}}

"""

# Create a classification tool
@tool
def classify_file(file_name: str) -> dict:
    """Classify the file based on its name."""
    prompt = PromptTemplate(input_variables=["file_name"], template=prompt_template)
    formatted_prompt = prompt.format(file_name=file_name)
    
    # Convert formatted prompt to the chat message format expected by ChatGroq
    messages = [{"role": "user", "content": formatted_prompt}]
    
    response = llm.invoke(messages)
    
    structured_response = response.content
    
    try:
        return json.loads(structured_response)
    except json.JSONDecodeError:
        # If response is not well-formed JSON, return "Others" as the default category
        return {"category": "Others"}

def create_category_directories(base_folder):
    """Create category directories inside the base folder"""
    for category in categories:
        os.makedirs(os.path.join(base_folder, category), exist_ok=True)

def organize_folder(base_folder):
    """Organize the folder into categorized subfolders"""
    create_category_directories(base_folder)
    
    # Scan the folder
    for file_name in tqdm(os.listdir(base_folder)):
 
            # Exclude already categorized folders
            if any(cat in base_folder for cat in categories):  
                continue
            
            file_path = os.path.join(base_folder, file_name)
            if os.path.isdir(file_path):
                # skip directories
                continue
            
            # Use file name only for classification
            classification = classify_file(file_name)["category"]
            #print(file_name, classification)
            target_folder = os.path.join(base_folder, classification)
            
            # Move file to the classified folder
            if classification in categories:
                shutil.move(file_path, target_folder)
                #print(f"Moved {file_name} to {classification}")
            else:
                # If the classification fails or is "Others", put it in the "Others" folder
                shutil.move(file_path, os.path.join(base_folder, "Others"))
                #print(f"Moved {file_name} to Others")

# Example usage
if __name__ == "__main__":
    base_folder = r"path/to/folder"
    organize_folder(base_folder)

# Folder Organizer using ChatGroq LLM

This repository contains a Python script that automatically organizes files in a given folder into specific categories based on their filenames. The script uses the ChatGroq language model (via Langchain) to classify files and move them into relevant subfolders. The categories are predefined, and any unclassified files are placed in an "Others" folder.

## Features
- **File Classification**: Files are classified based on their filenames into categories such as "Research Papers", "Documents", "Textbooks", etc.
- **Automatic Folder Creation**: Subfolders for each category are automatically created in the base folder if they don't exist.
- **File Organization**: Files are moved to their respective categorized folders, keeping your directory organized.
- **Progress Bar**: The script displays a progress bar to track the file organization process.

## Prerequisites

Before running the script, you need to:

1. Have Python 3.x installed on your system.
2. Install the necessary Python packages:

```bash
pip install langchain tqdm langchain_groq
```

3. Set your Groq API key as an environment variable:

```bash
export GROQ_API=your_api_key_here
```

## Categories
The script classifies files into the following predefined categories:

- Research Papers
- Documents
- Textbooks
- Images
- Audio Files
- Previous Year Papers
- Software
- Codes
- Others (default if no match is found)

## How It Works

1. **Classification**: The script uses a language model (ChatGroq) to classify file names into one of the predefined categories.
2. **Organization**: Files are moved into the respective category folders inside the base folder. If a file cannot be classified, it is placed in the "Others" folder.
3. **Directories Ignored**: The script only processes files in the given folder and ignores any directories inside it.

## Usage

1. **Set up your environment**:
   - Make sure you have your ChatGroq API key set as an environment variable.

2. **Place your files**:
   - Place all the files you want to organize inside a folder.

3. **Run the script**:
   - Modify the `base_folder` variable in the script to the path where your files are located.
   - Run the script:

   ```bash
   python app.py
   ```

4. The script will classify and organize the files in the base folder according to their filenames.

### Example:

```bash
base_folder = r"path/to/folder"
organize_folder(base_folder)
```

## Code Structure

### `classify_file(file_name: str) -> dict`
This function uses the ChatGroq language model to classify the file based on its name. It returns a JSON object with the category name.

### `create_category_directories(base_folder: str)`
This function creates directories for each category in the base folder if they don't exist.

### `organize_folder(base_folder: str)`
This function orchestrates the organization process. It scans the files in the base folder, classifies them, and moves them to the appropriate category folders.

## Example Folder Structure

Before running the script:
```
/my-folder
    paper1.pdf
    image.png
    audio.mp3
    code.py
```

After running the script:
```
/my-folder
    /Research Papers
        paper1.pdf
    /Images
        image.png
    /Audio Files
        audio.mp3
    /Codes
        code.py
```
Feel free to fork and modify the repository according to your needs! Contributions are welcome.


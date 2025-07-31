
# 📝 docxToMarkdown

A Python script to convert Microsoft Word `.docx` documents into clean, structured Markdown files.

## Features


- ✅ Converts headings to Markdown syntax (`#`, `##`, etc.)
- ✅ Supports bullet and numbered lists
- ✅ Converts tables to Markdown format
- ✅ Automatically removes inline images
- ✅ Batch processes all `.docx` files in a folder


## 📦 Installation

### 1. Clone and install
```bash
git clone https://github.com/yourusername/docxToMarkdown.git
cd docxToMarkdown
pip install .
```
### 2. Ore use in development
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```


## 🛠 Usage

Command-line:
```bash
docx-to-markdown /path/to/docx_folder [output_md_folder]
```
Or via Python:
```python
from docx_to_markdown.cli import main
main("/path/to/docx", "markdown_output")
```
- docx_folder: folder containing .docx files
- output_md_folder (optional): destination folder for .md files (default: md_docs)

## 📄 Example
```bash
docx-to-markdown ./word_docs ./markdown_docs
```

📂 Output
Each .docx file is converted into a .md file with the same name in the output folder.

🧪 Tests
Run the test suite with:

bash
```bash
pytest tests/
```

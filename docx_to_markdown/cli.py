from pathlib import Path
from .converter import word_to_markdown

def main(raw_docs: str, md_dir: str = 'md_docs') -> None:
    """
    Converts all .docx files in a given directory to Markdown (.md) files.

    Args:
        raw_docs (str): Path to the directory containing .docx files.
        md_dir (str, optional): Name of the output directory for Markdown files. Defaults to 'md_docs'.

    Raises:
        ValueError: If the provided path does not exist or is not a directory.

    This function scans the specified directory for .docx files, converts each to Markdown format,
    and saves the results in the specified output directory. If no .docx files are found, a message is printed.
    """
    raw_docs = Path(raw_docs)
    if not raw_docs.exists() or not raw_docs.is_dir():
        raise ValueError(f"Invalid path: {raw_docs}")

    docx_files = list(raw_docs.glob('*.docx'))
    if not docx_files:
        print('No .docx files found in the directory')
        return

    md_folder = Path.cwd() / md_dir
    md_folder.mkdir(parents=True, exist_ok=True)

    for docx_file in docx_files:
        try:
            output_file = md_folder / docx_file.with_suffix('.md').name
            markdown = word_to_markdown(str(docx_file))
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f'Converted {docx_file.name} -> {output_file.name}')
        except Exception as e:
            print(f'Error converting {docx_file.name}: {e}')
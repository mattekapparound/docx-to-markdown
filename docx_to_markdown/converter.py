import re
from pathlib import Path
from docx import Document
from .utils import iter_block_items, document_numbering_is_numbered
from docx.table import Table
from docx.text.paragraph import Paragraph

def word_to_markdown(doc_path: str) -> str:
    """
    Converts a .docx file to Markdown format.

    Args:
        doc_path (str): The path to the .docx file.

    Returns:
        str: The converted Markdown content as a string.
    """
    doc = Document(doc_path)
    md_lines = []

    for block in iter_block_items(doc):
        # Paragraph
        if isinstance(block, Paragraph):
            text = block.text.strip()
            style = block.style.name.lower()

            if not text and not block.runs:
                continue

            # Heading
            if style.startswith('heading'):
                level = int(re.search(r"\d+", style).group())
                md_lines.append('#' * level + ' ' + text)
                continue

            # Lists
            if block._p.pPr is not None and block._p.pPr.numPr is not None:
                ilvl = block._p.pPr.numPr.ilvl.val
                prefix = '  ' * ilvl
                num_id = block._p.pPr.numPr.numId.val
                bullet = '-' if not document_numbering_is_numbered(doc, num_id) else '1.'
                md_lines.append(f"{prefix}{bullet} {text}")
                continue

            # Inline images
            for run in block.runs:
                if run._element.findall('.//w:drawing',
                                           {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}):
                    md_lines.append('')
                    break
            if text:
                md_lines.append(text)

        # Tables
        elif isinstance(block, Table):
            rows = [[cell.text.strip() for cell in row.cells]
                    for row in block.rows if any(cell.text.strip() for cell in row.cells)]
            if not rows:
                continue
            header = rows[0]
            md_lines.append('| ' + ' | '.join(header) + ' |')
            md_lines.append('|' + '|'.join(' --- ' for _ in header) + '|')
            for data in rows[1:]:
                md_lines.append('| ' + ' | '.join(data) + ' |')

    return '\n'.join(md_lines)

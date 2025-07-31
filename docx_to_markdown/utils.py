from pathlib import Path
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P

def iter_block_items(doc):
    """
    Yield each paragraph or table element in document order.
    """
    body = doc.element.body
    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield Table(child, doc)

def document_numbering_is_numbered(doc, num_id):
    """
    True se il numbering num_id è numerato ("decimal"), False se "bullet".
    """
    numbering = doc.part.numbering_part.numbering_definitions._numbering
    for num in numbering.num_lst:
        if num.numId == str(num_id):
            abs_id = num.abstractNumId.val
            for abs_num in numbering.abstractNum_lst:
                if abs_num.abstractNumId == str(abs_id):
                    for lvl in abs_num.lvl_lst:
                        fmt = lvl.numFmt.val
                        return fmt not in ('bullet',)
    return False

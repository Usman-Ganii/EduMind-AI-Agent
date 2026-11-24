from io import BytesIO
from pypdf import PdfReader

def extract_pdf_text(pdf_bytes: bytes) -> str:
    """Extract selectable text from a PDF uploaded by the user."""
    reader = PdfReader(BytesIO(pdf_bytes))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n\n".join(pages)

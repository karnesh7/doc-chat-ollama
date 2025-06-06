import fitz  # PyMuPDF
import docx

def read_pdf(path):
    doc = fitz.open(path)
    return "".join(page.get_text() for page in doc)

def read_docx(path):
    doc = docx.Document(path)
    return "\n".join(para.text for para in doc.paragraphs)

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_document(file_path):
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    elif file_path.endswith(".txt"):
        return read_txt(file_path)
    else:
        return "Unsupported file type."
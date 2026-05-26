from pathlib import Path
from docx import Document


def get_word_files(folder_path: str):

    folder = Path(folder_path)

    return folder.glob("*.docx")


def read_file(file_path: str) -> str:

    doc = Document(file_path)

    full_text = []

    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)

    return "\n".join(full_text)
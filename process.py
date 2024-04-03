import mammoth


def extract_text_from_docx(doc_path):
    with open(doc_path, "rb") as file:
        result = mammoth.extract_raw_text(file)
        return result.value


path = "text_data/EMF_1.doc"
text = extract_text_from_docx(path)
print(text)

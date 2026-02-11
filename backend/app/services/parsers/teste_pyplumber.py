import pdfplumber

with pdfplumber.open("COMP_08-02-2026 154700.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(type(text))

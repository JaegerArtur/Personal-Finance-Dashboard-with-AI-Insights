from base_parser import BaseParser
import pdfplumber

class UnicredParser(BaseParser):
    def parse(self, file_path):
        transactions = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                print(type(text))

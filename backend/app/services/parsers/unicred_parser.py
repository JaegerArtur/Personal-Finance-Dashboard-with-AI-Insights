from base_parser import BaseParser
import pdfplumber, re
from ...dto.transaction_dto import TransactionDTO
from decimal import Decimal
from datetime import datetime

class UnicredParser(BaseParser):
    date_pattern = re.compile(r"^\d\d/\d\d/\d\d\d\d")
    money_pattern = re.compile(r"^\s*-?\s*\d+(?:\.\d{3})*,\d{2}")
    amount_pattern = re.compile(r"-?\s*\d+(?:\.\d{3})*,\d{2}")
    
    def merge_lines(self, lines: list[str]) -> list[str]:
        current = ""
        merged = []
        
        for line in lines:
            if self.date_pattern.match(line):
                if current:
                    merged.append(current)
                current = line

            elif self.money_pattern.match(line):
                current += " " + line

            else:
                continue

        if current:
            merged.append(current)

        return merged

    def parse_line(self, line: str) -> TransactionDTO | None:
        # Faz a pesquisa e armazena para reuso
        date_match = self.date_pattern.search(line)
        amount_match = self.amount_pattern.search(line)

        # Em caso de erro, retorna None
        if date_match is None or amount_match is None:
            return None

        # Converte texto para o formato datetime
        date = datetime.strptime(date_match.group(), "%d/%m/%Y")

        # Encontra os limites da descrição da transação
        last_date_position = date_match.span()[1]
        first_amount_position = amount_match.span()[0]
        description = line[last_date_position:first_amount_position].strip()

        amount = Decimal(amount_match.group().replace(' ', '').replace(",", "."))
        transaction_type = "income" if amount > 0 else "expense"

        return TransactionDTO(date=date, description=description or "SEM_DESCRICAO", amount=amount, category=None, transaction_type=transaction_type) 


    def parse(self, file_path: str) -> list[TransactionDTO]:
        transactions = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text is None:
                    continue
                lines = text.splitlines()
                merged = self.merge_lines(lines)
                
                for line in merged:
                    dto = self.parse_line(line)
                    if dto is not None:
                        transactions.append(dto)

        return transactions
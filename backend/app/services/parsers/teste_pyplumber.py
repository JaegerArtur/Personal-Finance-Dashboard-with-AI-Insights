import pdfplumber
import re
from ...dto.transaction_dto import TransactionDTO
from decimal import Decimal
from datetime import datetime

date_pattern = re.compile(r"^\d\d/\d\d/\d\d\d\d")
money_pattern = re.compile(r"^\s*-?\s*\d+(?:\.\d{3})*,\d{2}")
amount_pattern = re.compile(r"-?\s*\d+(?:\.\d{3})*,\d{2}")

def merge_lines(lines: list[str]) -> list[str]:
    current = ""
    merged = []
    
    for line in lines:
        if date_pattern.match(line):
            if current:
                merged.append(current)
            current = line

        elif money_pattern.match(line):
            current += " " + line

        else:
                continue

    if current:
        merged.append(current)

    return merged

def parse_line(line: str) -> TransactionDTO | None:
    # Faz a pesquisa e armazena para reuso
    date_match = date_pattern.search(line)
    amount_match = amount_pattern.search(line)

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

with pdfplumber.open("COMP_08-02-2026 154700.pdf") as pdf:
    for page in pdf.pages:
        lines = page.extract_text().splitlines()
        transactions = []
        merged = merge_lines(lines)
        
        for line in merged:
            transactions.append(parse_line(line))


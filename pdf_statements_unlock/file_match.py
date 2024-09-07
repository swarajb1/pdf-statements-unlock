from core.config import settings
from database.enums import BankCreditCards

from typing import Final

data_passwords: Final[dict[BankCreditCards, str]] = {
    BankCreditCards.ICICI_BANK: settings.ICICI_PDF_PASSWORD,
    BankCreditCards.HDFC_BANK: settings.HDFC_PDF_PASSWORD,
    BankCreditCards.KOTAK_BANK: settings.KOTAK_PDF_PASSWORD,
    BankCreditCards.STANDARD_CHARTERED_BANK: settings.STANDARD_CHARTERED_PDF_PASSWORD,
}


file_name_match: Final[dict[BankCreditCards, list[str]]] = {
    BankCreditCards.ICICI_BANK: ["coral", "amazon"],
    BankCreditCards.HDFC_BANK: ["4854xx"],
    BankCreditCards.KOTAK_BANK: ["300xxx8403-484552"],
    BankCreditCards.STANDARD_CHARTERED_BANK: ["eStatement3531"],
}


def get_pdf_password(file_name: str) -> tuple[BankCreditCards, str]:
    for bank, values in file_name_match.items():
        for value in values:
            if value.lower() in file_name.lower():
                return bank, data_passwords[bank]

    raise ValueError(f"Password not found for the given file name - {file_name}")

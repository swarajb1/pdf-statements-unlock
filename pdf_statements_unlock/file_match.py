from database.card_management import card_matrix
from database.enums import BankCreditCards


def get_pdf_password(file_name: str) -> tuple[BankCreditCards, str]:
    card_name_prefix: str = ""

    for bank in card_matrix:
        cards = card_matrix[bank]["cards"]

        for card in cards:
            for file_match in card.file_name_match:
                if file_match.lower() in file_name.lower():
                    if not card_matrix[bank]["pdf_password"]:
                        raise ValueError(f"Password is null for the given file name - {file_name}")

                    return bank, card_matrix[bank]["pdf_password"], card

    raise ValueError(f"Password not found for the given file name - {file_name}")

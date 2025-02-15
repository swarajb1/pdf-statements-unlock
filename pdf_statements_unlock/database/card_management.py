from typing import Generic, NamedTuple, TypeVar

from core.config import settings
from database.enums import BankCreditCards, StateEnum

StatesEnum = TypeVar("StatesEnum", bound=StateEnum, contravariant=True)


class CardData:
    def __init__(self, number: str, name: str, file_name_match: list[str]):
        self.number = number
        self.name = name
        self.file_name_match = file_name_match


class StateData(NamedTuple, Generic[StatesEnum]):
    cards: list[CardData]
    pdf_password: str


class CardMatrix(dict, Generic[StatesEnum]):
    def __getitem__(self, k: StatesEnum) -> StateData[StatesEnum]:
        return super().__getitem__(k)


card_matrix: CardMatrix[BankCreditCards] = {
    BankCreditCards.ICICI_BANK: CardMatrix(
        cards=[
            CardData(
                number=settings.ICICI_CARD_1_NUMBER,
                name=settings.ICICI_CARD_1_NAME,
                file_name_match=["amazon"],
            ),
            CardData(
                number=settings.ICICI_CARD_2_NUMBER,
                name=settings.ICICI_CARD_2_NAME,
                file_name_match=["xx1005"],
            ),
            CardData(
                number=settings.ICICI_CARD_3_NUMBER,
                name=settings.ICICI_CARD_3_NAME,
                file_name_match=["xx6003"],
            ),
        ],
        pdf_password=settings.ICICI_PDF_PASSWORD,
    ),
    BankCreditCards.HDFC_BANK: CardMatrix(
        cards=[
            CardData(
                number=settings.HDFC_CARD_1_NUMBER,
                name=settings.HDFC_CARD_1_NAME,
                file_name_match=["4341xx"],
            ),
            CardData(
                number=settings.HDFC_CARD_2_NUMBER,
                name=settings.HDFC_CARD_2_NAME,
                file_name_match=["5268xx"],
            ),
            CardData(
                number=settings.HDFC_CARD_3_NUMBER,
                name=settings.HDFC_CARD_3_NAME,
                file_name_match=["4023xx"],
            ),
        ],
        pdf_password=settings.HDFC_PDF_PASSWORD,
    ),
    BankCreditCards.KOTAK_BANK: CardMatrix(
        cards=[
            CardData(
                number=settings.KOTAK_CARD_1_NUMBER,
                name=settings.KOTAK_CARD_1_NAME,
                file_name_match=["300xxx8403-484552"],
            ),
        ],
        pdf_password=settings.KOTAK_PDF_PASSWORD,
    ),
    BankCreditCards.STANDARD_CHARTERED_BANK: CardMatrix(
        cards=[
            CardData(
                number=settings.STANDARD_CHARTERED_CARD_1_NUMBER,
                name=settings.STANDARD_CHARTERED_CARD_1_NAME,
                file_name_match=["eStatement3531", "STANCHART"],
            ),
        ],
        pdf_password=settings.STANDARD_CHARTERED_PDF_PASSWORD,
    ),
    BankCreditCards.INDUSIND_BANK: CardMatrix(
        cards=[
            CardData(
                number=settings.INDUSIND_CARD_1_NUMBER,
                name=settings.INDUSIND_CARD_1_NAME,
                file_name_match=["--"],
            ),
        ],
        pdf_password=settings.INDUSIND_PDF_PASSWORD,
    ),
}

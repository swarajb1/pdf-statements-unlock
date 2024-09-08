from enum import Enum


class StateEnum(Enum):
    pass


class BankCreditCards(StateEnum, Enum):
    ICICI_BANK = "ICICI Bank"
    HDFC_BANK = "HDFC Bank"
    KOTAK_BANK = "Kotak Bank"
    STANDARD_CHARTERED_BANK = "Standard Chartered Bank"

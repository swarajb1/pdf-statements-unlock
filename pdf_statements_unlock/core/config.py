import logging
from enum import StrEnum, auto
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.config import Config

ENV_FILEPATH: Path = Path(find_dotenv())

load_dotenv(ENV_FILEPATH)
config: Config = Config(ENV_FILEPATH)


class EnvFlavour(StrEnum):
    dev = auto()
    prod = auto()


class GlobalConfig(BaseSettings):
    """Global configurations."""

    PROJECT_NAME: str = Field(default="pdf_statements_unlock")

    VERSION: str = "1.0"

    FLAVOUR: EnvFlavour = Field(default=EnvFlavour.dev)

    DEBUG: bool = Field(default=False)
    LOGGING_LEVEL: int = logging.DEBUG if DEBUG else logging.INFO

    ICICI_PDF_PASSWORD: str

    HDFC_PDF_PASSWORD: str

    KOTAK_PDF_PASSWORD: str

    STANDARD_CHARTERED_PDF_PASSWORD: str

    INDUSIND_PDF_PASSWORD: str

    ICICI_CARD_1_NUMBER: str
    ICICI_CARD_1_NAME: str

    ICICI_CARD_2_NUMBER: str
    ICICI_CARD_2_NAME: str

    ICICI_CARD_3_NUMBER: str
    ICICI_CARD_3_NAME: str

    ICICI_CARD_4_NUMBER: str
    ICICI_CARD_4_NAME: str

    KOTAK_CARD_1_NUMBER: str
    KOTAK_CARD_1_NAME: str

    HDFC_CARD_1_NUMBER: str
    HDFC_CARD_1_NAME: str

    HDFC_CARD_2_NUMBER: str
    HDFC_CARD_2_NAME: str

    HDFC_CARD_3_NUMBER: str
    HDFC_CARD_3_NAME: str

    STANDARD_CHARTERED_CARD_1_NUMBER: str
    STANDARD_CHARTERED_CARD_1_NAME: str

    INDUSIND_CARD_1_NUMBER: str
    INDUSIND_CARD_1_NAME: str

    model_config = SettingsConfigDict()


class DevConfig(GlobalConfig):
    """Development configurations."""

    DEBUG: bool = True


class ProdConfig(GlobalConfig):
    """Production configurations."""


class FactoryConfig:
    """Returns a config instance depending on the env FLAVOUR variable."""

    def __init__(self, flavour: EnvFlavour):
        self.FLAVOUR = flavour

    def __call__(self) -> GlobalConfig:
        config: type[GlobalConfig] = GlobalConfig

        if self.FLAVOUR == EnvFlavour.dev:
            config = DevConfig

        elif self.FLAVOUR == EnvFlavour.prod:
            config = ProdConfig

        return config.model_validate({})


settings: GlobalConfig = FactoryConfig(
    config("FLAVOUR", default=EnvFlavour.dev, cast=EnvFlavour)
)()

__all__ = ["settings"]

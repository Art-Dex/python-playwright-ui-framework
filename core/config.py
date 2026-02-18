from enum import Enum
from functools import lru_cache
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    chromium = "chromium"
    firefox = "firefox"
    webkit = "webkit"


class Environment(str, Enum):
    dev = "dev"
    stage = "stage"
    prod = "prod"


class Settings(BaseSettings):
    """
    Конфигурация приложения.

    Приоритет:
    1. Переменные окружения
    2. .env файл
    3. Значения по умолчанию
    """

    # --- Основные настройки ---
    base_url: HttpUrl
    environment: Environment = Environment.dev

    # --- Настройки браузера ---
    browser: Browser = Browser.chromium
    headless: bool = True
    slow_mo: Optional[int] = 0
    timeout: int = 10000

    @field_validator("slow_mo")
    @classmethod
    def validate_slow_mo(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 0:
            raise ValueError("slow_mo должен быть >= 0")
        return value

    @field_validator("timeout")
    @classmethod
    def validate_timeout(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("timeout должен быть > 0")
        return value

    @property
    def is_prod(self) -> bool:
        return self.environment == Environment.prod

    @property
    def is_stage(self) -> bool:
        return self.environment == Environment.stage

    @property
    def is_dev(self) -> bool:
        return self.environment == Environment.dev

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # игнорировать лишние переменные
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

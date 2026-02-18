from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    base_url: str = "https://www.saucedemo.com"
    browser: str = "chromium"
    headless: bool = True

    class Config:
        env_file = ".env"


settings = Settings()

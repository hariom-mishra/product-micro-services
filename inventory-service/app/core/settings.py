from urllib.parse import quote_plus
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_USER: str
    DB_PASSWORD: str = ""
    DB_NAME: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    @computed_field
    @property
    def DB_URL(self) -> str:
        if self.DB_PASSWORD:
            resolved_pass = quote_plus(self.DB_PASSWORD)
            return f"postgresql+asyncpg://{self.DB_USER}:{resolved_pass}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()




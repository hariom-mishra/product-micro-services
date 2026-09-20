from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote_plus
from pydantic import computed_field

class Settins(BaseSettings):
    model_config = SettingsConfigDict(env_file= ".env", extra= 'ignore')

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    INVENTORY_SERVICE_URL: str

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        if self.DB_PASSWORD:
            password = quote_plus(self.DB_PASSWORD)
            return f"postgresql+asyncpg://{self.DB_USER}:{password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            return f"postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        

settings = Settins()
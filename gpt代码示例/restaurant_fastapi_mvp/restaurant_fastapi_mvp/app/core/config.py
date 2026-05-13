from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    APP_NAME: str = "Restaurant Analytics MVP"
    APP_ENV: str = Field(default="dev")
    APP_VERSION: str = Field(default="0.1.0")
    API_V1_PREFIX: str = Field(default="/api/v1")
    DEBUG: bool = Field(default=True)

    JWT_SECRET_KEY: str = Field(default="change-this-in-production-at-least-32-chars")
    JWT_ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=120)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Restaurant MVP API"
    app_env: str = "dev"
    debug: bool = True

    api_v1_prefix: str = "/api/v1"

    jwt_secret_key: str = "replace_with_a_very_long_secure_secret_key_for_dev_only_123456"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_secret_key: str = "replace_with_a_refresh_secret_for_dev_only_123456"
    jwt_refresh_token_expire_days: int = 7
    login_max_failed_attempts: int = 5
    login_lock_minutes: int = 1
    database_url: str = "postgresql+psycopg://placeholder:placeholder@localhost:5432/placeholder_db"


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()

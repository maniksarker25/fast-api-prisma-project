from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    APP_ENV: str = "development"
    APP_NAME: str = "Enterprise FastAPI Backend"
    SECRET_KEY: str = "change-me-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    REDIS_URL: str = "redis://localhost:6379"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "fastapi_db"


settings = Settings()

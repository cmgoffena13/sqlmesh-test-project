from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SLACK_WEBHOOK_URL: str
    GOOGLE_PROJECT: str
    CLOUD_SQL_INSTANCE_CONNECTION_STRING: str
    CLOUD_SQL_USER: str
    CLOUD_SQL_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()  # type: ignore

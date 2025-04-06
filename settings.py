from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GRAFANA_HOST: str
    GRAFANA_PORT: str

    GRAFANA_LOGIN: str
    GRAFANA_PASSWORD: str

    CLICKHOUSE_HOST: str
    CLICKHOUSE_PORT: str
    CLICKHOUSE_USER: str
    CLICKHOUSE_PASSWORD: str

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()

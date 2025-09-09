from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # DB Settings
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"


settings = Settings()


if __name__ == "__main__":
    print(settings.POSTGRES_PASS)
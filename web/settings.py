from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # DB Settings
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_DB: str

    @property
    def database_url(self):
        user = f"{self.POSTGRES_USER}:{self.POSTGRES_PASS}"
        database = f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

        return f"postgresql+asyncpg://{user}@{database}"
    
    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()


if __name__ == "__main__":
    print(settings.database_url)
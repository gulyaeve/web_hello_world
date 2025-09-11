from pydantic_settings import BaseSettings
from urllib.parse import quote
from faststream.rabbit import RabbitBroker


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
    
    # RabbitMQ parameters
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_VHOST: str

    @property
    def rabbitmq_url(self) -> str:
        user = f"{self.RABBITMQ_USER}:{quote(self.RABBITMQ_PASS)}"
        server = f"{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"
        return (
            f"amqp://{user}@{server}"
        )
    
    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str

    # Bearer auth
    TOKEN_BEARER: str

    class Config:
        env_file = ".env"


settings = Settings()

broker = RabbitBroker(settings.rabbitmq_url, virtualhost=settings.RABBITMQ_VHOST)


if __name__ == "__main__":
    print(settings.database_url)
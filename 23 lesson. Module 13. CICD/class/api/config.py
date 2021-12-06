import os


class Config:
    DEBUG = False
    TESTING = False

    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD_TEST")
    POSTGRES_USER = os.getenv("POSTGRES_USER_TEST")
    POSTGRES_DB = os.getenv("POSTGRES_DB_TEST")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{Config.POSTGRES_HOST}:{Config.POSTGRES_PORT}/{POSTGRES_DB}"

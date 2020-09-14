import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", 'anydfsfsafaga')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    PRESERVE_CONTEXT_ON_EXCEPTION = False

    SESSION_COOKIE_SECURE = False

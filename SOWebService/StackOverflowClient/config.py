class Config(object):
    DEBUG = False
    TESTING = False
    START_DATE = "2008-08-01"
    DUMP_DATE = "2019-08-31"
    WS_HOST = "localhost"
    WS_PORT = 19000


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

import os

class Config:
    """
    General configuration child class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:123@localhost/pitch2'
    

class ProdConfig(Config):
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
# # class TestConfig(Config):
# #     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:123@localhost/pitches_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:123@localhost/pitch2'

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    # 'test': TestConfig
}
    
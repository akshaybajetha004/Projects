import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # for github and social login authetication
    GOOGLE_CLIENT_ID = "914289289455-5rjsumgscqpk517jau7p2tgbtmc5cm1c.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "sOEYMolWR57j9XOEx96If93Y"
    GITHUB_CLIENT_ID = "654d427fc257e7de4c92"
    GITHUB_CLIENT_SECRET = "dd0e20e51e988523d5e05c51241297e876929f4a"

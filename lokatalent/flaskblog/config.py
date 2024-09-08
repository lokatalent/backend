import os


class Config:
    SECRET_KEY = '54a3816e9f4df0de4bec9556bfcd73940cb7ce7b283ad326cacd55cdb8429b30'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "gabeamazing21@gmail.com"
    MAIL_PASSWORD = "Skysuccess@#$><1"
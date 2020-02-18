import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SECRET_KEY = "977F06E9E47674000CD2D73632741C9C43486246"
    SECURITY_PASSWORD_SALT = "5916E01239D67D53D47F461F5DE05BBD00E924A6"
    SECURITY_PASSWORD_HASH = "sha512_crypt"
    FTP_USER = "ftp.user"
    FTP_HOST = "connect.as-electrica.ru"
    FTP_PORT = 89
    FTP_PASSWORD = "Kl@yped@"




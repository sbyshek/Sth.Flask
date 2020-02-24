from config import Configuration
from ftplib import FTP


def download_from_remote_ftp_server():
    ftp = FTP(host="connect.as-electrica.ru", user="ftp.user", passwd="Kl@yped@")
    ftp.port = "89"
    # ftp.host = Configuration.FTP_HOST
    ftp.port = Configuration.FTP_PORT
    # ftp.login(user=Configuration.FTP_USER, passwd=Configuration.FTP_PASSWORD)
    ftp.connect()
    # print(ftp)


def main():
    download_from_remote_ftp_server()


if __name__ == '__main__':
    main()



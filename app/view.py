from app import app
from flask import render_template
from ftplib import FTP


@app.route("/")
def index():
    name = "Bob"
    return render_template("index.html", var=name)


@app.route("/download")
def download():

    pass


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


def main():
    download_from_remote_ftp_server()


if __name__ == "__main__":
    main()


from ftplib import FTP

def ftp_operations():
    ftp_server="ftp.dlptest.com"
    username="dlpuser"
    password="rNrKYTX9g7z3RgJRmxWuGHbeu"

    ftp=FTP(ftp_server)
    ftp.login(user=username, passwd=password)

    # Upload file
    filename="file.txt"
    with open(filename, "rb") as f:
        ftp.storbinary(f"STOR {filename}", f)
    print("File uploaded.")

    # Download file
    download_file="file.txt"
    with open("local_download.txt", "wb") as f:
        ftp.retrbinary(f"RETR {download_file}", f.write)
    print("File downloaded.")

    # List directory
    print("Directory contents:")
    ftp.dir()

    ftp.quit()

ftp_operations()

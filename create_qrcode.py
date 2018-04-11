import qrcode
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url",help="give the download_app url")
parser.add_argument("file_path",help="give the file_path of qrcode")
args = parser.parse_args()

def create_qrcode(filepath,url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=2,
        border=1
    )
    qr.add_data(url)
    qr.make()
    img = qr.make_image()
    img.save(filepath)


if __name__ == "__main__":
    create_qrcode(args.file_path,args.url)
import qrcode123
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
    img = qr.make_image()54
    img.save(filepath)
    
def create_qrcode(filepath,url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=2,
        border=1
    )
    qr.add_data(url)
    qr.make()
    img = qr.make_image()54
    img.save(filepath)
def test:
    print"this is a test"
微软微软
123123
789
werwe
12312783
23434
微软微软
123123
if __name__ == "__main__":
    create_qrcode(args.file_path,args.url)

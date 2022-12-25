# pip install PyQRCode
# pip install pypng

import pyqrcode
link = "https://github.com/solitkas"
qr_code = pyqrcode.create(link)
qr_code.png("test.png", scale=5)



# pip install pyzbar
# pip install pillow
def Decode(png: str):
    from pyzbar.pyzbar import decode
    from PIL import Image
    decode_qr = decode(Image.open(png))
    print(decode_qr[0].data.decode('ascii'))



# pip install PyQRCode
# pip install pypng

import pyqrcode
link = "https://github.com/solitkas"
qr_code = pyqrcode.create(link)
qr_code.png("test.png", scale=5)


import pyqrcode

data = "www.google.com"

url = pyqrcode.create(data)
url.svg("qrcodephoto.svg", scale=8)

url.png("myqrcode.png", scale=10)
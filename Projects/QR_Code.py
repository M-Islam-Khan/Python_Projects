import qrcode

img = qrcode.make("https://youtu.be/kHNCaWjB-98")
img.save("myQRcode.png")
img.show()

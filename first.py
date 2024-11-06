import qrcode as qr

img = qr.make("https://www.youtube.com/@rohitkumre6435")
img.save("mycode.png")
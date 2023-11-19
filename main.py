import qrcode
print("MADE BY : BERGERER")
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

data = input("data : ")

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

if img.save("qr_code.png"):
	print("done!")
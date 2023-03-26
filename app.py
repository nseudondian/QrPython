import qrcode

def gen_qr(text):
    

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url = input("Type your url: ")
# gen_qr("https://www.migrant-solutions.com")
gen_qr(url)
import qrcode
from PIL import Image


vcard_data = """BEGIN:VCARD
VERSION:3.0
N:Ayikwei;Richard;;Mr.;
FN:Richard Ayikwei
ORG:Kofa Technologies Limited
TITLE:Network Management Associate
TEL:+233509805280
EMAIL:richard.ayikwei@kofa.co
URL:https://www.linkedin.com/in/richard-ayikwei-48b171112
END:VCARD"""

qr = qrcode.QRCode(
    version=None,  # auto
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,
    border=4
)

qr.add_data(vcard_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img = img.resize((500, 500), Image.LANCZOS)
img.save("richard_ayikwei_vcard.png")

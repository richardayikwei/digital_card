import qrcode
from PIL import Image

vcard_data = """
BEGIN:VCARD
VERSION:3.0
N:Ayikwei;Richard
FN:Richard Ayikwei
ORG:Kofa Technologies Limited
URL:https://www.linkedin.com/in/richard-ayikwei-48b171112
EMAIL:richard.ayikwei@kofa.co
TEL:+233509805280
TITLE:Network Management Associate
END:VCARD
"""

qr = qrcode.QRCode(
    version=None,  # auto
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,
    border=4
)

qr.add_data(vcard_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img = img.resize((300, 300), Image.LANCZOS)
img.save("richard_ayikwei_vcard.png")

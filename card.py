import qrcode

url = "https://raw.githubusercontent.com/YOUR_USERNAME/digital-card/main/richard_ayikwei.vcf"  # or Google Drive link
img = qrcode.make(url)
img.save("richard_vcard_qr.png")

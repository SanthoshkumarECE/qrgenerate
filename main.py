import qrcode

features = qrcode.QRCode(version=1, box_size=50, border=3)
features.add_data('http://www.youtube.com')
features.make(fit=True)
generate_image = features.make_image(fill_colour="black", back_colour="yellow")
generate_image.save('image2.png')
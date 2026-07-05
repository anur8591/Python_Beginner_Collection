# need two libraries to generate QR codes in python:
# 1. pip install qrcode (library for generating QR codes)
# 2. pip install pillow (library  for handling images)

import qrcode

# Taking upi id as a input from the user 
upi_id = input('please enter or paste your UPI ID: ')

generate_qr = qrcode.make(upi_id)  # generating QR code for the given UPI ID
# generate_qr.save("upi_qr_code.jpg")
generate_qr.show()






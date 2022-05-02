import qrcode 
from PIL import Image
from barcode import Code39

while(1):
    print("---Menu---")
    print("1. QR Code Gen")
    print("2. Barcode Gen")
    print("3. Quit")
    choice = input()
    choice = int(choice)

    if choice == 3:
        exit()

    if choice == 1:

        img = input("Enter string to converted into QR Code\n")

        qr = qrcode.QRCode(
            version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
             border=4,
        )

        qr.add_data(img)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white').convert('RGB')
        img.save('sample.png')

    if choice == 2:

        num = input('Enter Code: \n')
        name = input("Enter Student Name: \n")

        numCode = Code39(num)
        numCode.save(name)

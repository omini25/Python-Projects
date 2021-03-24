import pyqrcode


def qrcode():
    q = pyqrcode.create(input("Enter text you want converted to qrcode: "))
    q.png('qrcode.png', scale=6)
    print('QR Code Generated')


if __name__ == '__main__':
    qrcode()

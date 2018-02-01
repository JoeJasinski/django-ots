import qrcode


def gen_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    return img

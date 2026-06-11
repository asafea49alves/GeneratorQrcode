import qrcode
import sys

def generate_qr_code(data, filename):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python GeneratorImage.py <data> <filename>")
        sys.exit(1)
    data = sys.argv[1]
    filename = sys.argv[2]

    generate_qr_code(data, filename)
    print(f"QR code generated and saved as {filename}")
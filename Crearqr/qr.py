import qrcode
from PIL import Image

# Datos del QR
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdjuxkT4aS95iXZipiENo5VMVcl50FyCZj-3eUxXhb4Ccfplw/viewform'
logo_path = 'Logo Cetis.png'
output_path = 'qr_logo_cetis.png'

# Generar QR
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Abrir logo y ajustar tamaño
logo = Image.open(logo_path)
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.22)  # 22% del QR
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calcular posición y pegar logo
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Guardar resultado
qr_img.save(output_path)
print('Listo: qr_logo_cetis.png')
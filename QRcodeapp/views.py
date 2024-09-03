from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO
import base64

def generate_qr(request):
    qr_image = None
    
    if request.method == "POST":
        data = request.POST.get('qr_text', 'Default Text')

        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=4,
            border=4,
        )
        qr_code.add_data(data)
        qr_code.make(fit=True)

        img = qr_code.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        # Encode image to base64 string to display on the webpage
        qr_image = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'generate_qr.html', {'qr_image': qr_image})

import base64
from django.core.files.base import ContentFile

def handle_kyc_photo(data_uri):
    if not data_uri:
        return None
    try:
        format, imgstr = data_uri.split(';base64,')
        ext = format.split('/')[-1]
        return ContentFile(base64.b64decode(imgstr), name=f'kyc_photo.{ext}')
    except Exception:
        return None

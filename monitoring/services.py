import base64
import os
import re
from django.conf import settings

EVIDENCE_DIR = os.path.join(settings.BASE_DIR, "evidence/")
os.makedirs(EVIDENCE_DIR, exist_ok=True)


def save_evidence_image(mac, date, base64_image):
    # Substituir caracteres inválidos no nome do arquivo
    sanitized_mac = re.sub(r"[^\w\-]", "_", mac)
    timestamp = date.strftime("%Y%m%d%H%M%S")
    filename = f"{sanitized_mac}_{timestamp}.jpeg"
    evidence_path = os.path.join(EVIDENCE_DIR, filename)

    # Decodificar a imagem base64 e salvar no disco
    format, imgstr = base64_image.split(";base64,")
    with open(evidence_path, "wb") as img_file:
        img_file.write(base64.b64decode(imgstr))

    return evidence_path

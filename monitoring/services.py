import base64
import os
import re
from django.conf import settings
from datetime import datetime

EVIDENCE_DIR = os.path.join(settings.BASE_DIR, "evidence/")
os.makedirs(EVIDENCE_DIR, exist_ok=True)


def save_evidence_image(mac, date, evidence_base64):
    # Sanitizar o MAC removendo caracteres inválidos
    sanitized_mac = re.sub(
        r"[^a-zA-Z0-9]", "-", mac
    )  # Substitui caracteres inválidos por hifens

    # Criar a pasta onde a evidência será salva
    folder_path = os.path.join(settings.MEDIA_ROOT, "evidence")
    os.makedirs(folder_path, exist_ok=True)

    # Gerar o nome do arquivo
    filename = f"{sanitized_mac}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    file_path = os.path.join(folder_path, filename)

    # Decodificar o base64 e salvar a imagem
    try:
        with open(file_path, "wb") as image_file:
            image_file.write(base64.b64decode(evidence_base64))
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar a imagem de evidência: {e}")

    # Retornar o caminho relativo para salvar no banco de dados
    return f"evidence/{filename}"

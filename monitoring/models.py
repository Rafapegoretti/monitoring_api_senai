from django.db import models


class MonitoringEvent(models.Model):
    mac = models.CharField(max_length=17)  # Ex: XX:XX:XX:XX:XX:XX
    date = models.DateTimeField()  # Data do evento
    object_class = models.CharField(max_length=255)  # Classe do objeto detectado
    evidence = models.ImageField(
        upload_to="evidences/"
    )  # Caminho da imagem de evidência

    def __str__(self):
        return f"{self.object_class} detected at {self.date} from {self.mac}"

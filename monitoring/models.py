from django.db import models


class MonitoringData(models.Model):
    mac = models.CharField(max_length=50)
    date = models.DateTimeField()
    object_class = models.CharField(max_length=100)
    evidence_path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.mac} - {self.object_class} - {self.date}"

from django.db import models


# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=255, verbose_name="Status")
    code = models.CharField(max_length=20, verbose_name="Código")

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
        ordering = ['status']

    def __str__(self):
        return self.status


class Occurrence(models.Model):
    name = models.CharField(max_length=50)
    status = models.ForeignKey(Status, verbose_name="Status", on_delete=models.CASCADE, null=False)
    lon = models.FloatField()
    lat = models.FloatField()

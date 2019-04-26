from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=255, verbose_name="Status")
    codigo_waze = models.CharField(max_length=20, verbose_name="Cód WAZE", blank=True)
    codigo_cet = models.CharField(max_length=20, verbose_name="Cód CET", blank=True)
    codigo_css = models.CharField(max_length=20, verbose_name="Cód CSS")

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
        ordering = ['status']

    def __str__(self):
        return self.status


class Occurrence(models.Model):
    name = models.CharField(max_length=50)
    status = models.ForeignKey(Status, verbose_name="Status", on_delete=models.CASCADE, blank=False)
    lon = models.FloatField()
    lat = models.FloatField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.status)

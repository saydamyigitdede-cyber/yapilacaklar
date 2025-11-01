from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Gorev(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True, null=True)
    tamamlandi = models.BooleanField(default=False)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    yapilma_tarihi = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.baslik

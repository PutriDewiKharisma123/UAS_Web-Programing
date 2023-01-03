from django.db import models

# Create your models here.
class Produk(models.Model):
    Nama  = models.CharField(max_length=100)
    Jenis   = models.CharField(max_length=100)
    Harga   = models.CharField(max_length=100)

    def __str__(self):
        return "{}.{}" .format(self.id, self.Nama)
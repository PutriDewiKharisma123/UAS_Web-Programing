from django import forms
from .models import Produk

class Produkfrom(forms.ModelForm):
    class Meta:
        model = Produk
        fields = [
            'Nama',
            'Jenis',
            'Harga',
        ]
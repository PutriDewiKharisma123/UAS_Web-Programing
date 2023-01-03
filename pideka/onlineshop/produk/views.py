from django.shortcuts import render
from django.http import HttpResponseRedirect


from .models import Produk
from .forms import Produkfrom

def index(request):
    posts = Produk.objects.all()
    content = {
        'title': 'Sistem Informasi Manajemen Akademik Terpadu',
        'posts' : posts,
    }
    return render(request, 'produk/index.html', content)



   
def create(request):
    posts = Produk.objects.all()
    form = Produkfrom(request.POST or None)
    context = {
        'title' : 'produk',
        'form' :form,
        'posts' : posts,
    }
    if request.method =='POST':
        if form.is_valid():
            form.save()

          
        return HttpResponseRedirect("/produk/")

   

    return render(request, 'Produk/create.html', context) 





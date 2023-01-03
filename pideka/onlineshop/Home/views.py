from django.shortcuts import render

# Create your views here

def index(request):
  
    content = {
        'title': 'Produk',
        
        
    }
    return render(request, 'home/index.html', content)
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)

def details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'details.html', context)

def addProduct(request):
    try:
        newProduct = Product(
                                product_name=request.POST['product_name'],
                                product_description=request.POST['product_description'],
                                product_price=request.POST['product_price']
                            )
        newProduct.save()
        return HttpResponseRedirect('/')
    except: 
        return HttpResponseRedirect('/')

    
def deleteProduct(request, product_id):
    deletingProduct = Product.objects.get(id=product_id)
    deletingProduct.delete()
    return HttpResponseRedirect('/')
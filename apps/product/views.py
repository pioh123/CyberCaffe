from django.shortcuts import render, redirect
from .models import Product, Advertise
from .form import ProductForm, AdvertiseForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy




# Create your views here.


def listProduct(request):
    query = request.GET.get('search')
    products = Product.objects.all()
    if query:
        products = Product.objects.filter(
            Q(name__icontains = query)
        )
    paginator = Paginator(products,10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request,'product/list.html',{'products':products})

class AddProduct(CreateView):
    model = Product
    template_name = 'product/product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list_product')

class EditProduct(UpdateView):
    model = Product
    template_name = 'product/product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list_product')
    

def deleteProduct(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('product:list_product')

def quantityProduct(request):
    quantity = request.POST.get('quantity')
    productId = request.POST.get('productId')
    product = Product.objects.get(id = productId)
    product.stock = product.stock + int(quantity)
    product.save()
    return redirect('product:list_product')

def listAdvertise(request):
    advertises = Advertise.objects.all()
    
    
    return render(request,'product/listAd.html',{'advertises':advertises})

class EditAdvertise(UpdateView):
    model = Advertise
    template_name = 'product/ad.html'
    form_class = AdvertiseForm
    success_url = reverse_lazy('product:list_advertise')

    #def get_initial(self):
    #    return {'typea':4}


def addAdvertise(request):
    if request.method == 'POST':
        user_form = AdvertiseForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect('product:list_advertise')
    return redirect('product:list_advertise')

def deleteAdvertise(request, id):
    advertise = Advertise.objects.get(id = id)
    advertise.delete()
    return redirect('product:list_advertise')

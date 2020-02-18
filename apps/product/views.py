from django.shortcuts import render, redirect
from rest_framework import generics
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Product, Advertise,Promotion
from .form import ProductForm, AdvertiseForm,PromotionForm
from .serializer import ProductSerializer, AdvertiseSerializer,PromotionSerializer



# Create your views here.
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class AdvertiseListAPI(generics.ListCreateAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
class PromotionListAPI(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


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


class AddPromotion(CreateView):
    model = Promotion
    template_name = 'product/promotion.html'
    form_class = PromotionForm
    success_url = reverse_lazy('product:list_promotion')
    
class ListPromotion(ListView):
    model = Promotion
    context_object_name = 'promotions'
    template_name = 'product/listpromotion.html'
    queryset = Promotion.objects.all()

class EditPromotion(UpdateView):
    model = Promotion
    template_name = 'product/promotion.html'
    form_class = PromotionForm
    success_url = reverse_lazy('product:list_promotion')

from django.shortcuts import render, redirect
from rest_framework import generics
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product, Advertise
from .form import ProductForm, AdvertiseForm
from .serializer import ProductSerializer



# Create your views here.
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

class Login(FormView):
    template_name = "user/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('product:product_list_API')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request,format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)


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

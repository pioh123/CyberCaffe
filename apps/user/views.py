from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
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
from .models import Customer
from .form import UserForm, LoginAdminForm, CustomerForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

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

# Create your views here.
#def home(request):
 #   return render(request, 'user/home.html')
class RegisterUser(CreateView):
    model = User
    template_name = "user/register.html"
    form_class = UserForm
    success_url = reverse_lazy('home_n')

class RegisterCustomer(CreateView):
    model = Customer
    template_name = "user/register.html"
    form_class = CustomerForm
    success_url = reverse_lazy('home_n')

   


class Home(TemplateView):
    template_name = 'user/home.html'

class ListUser(ListView):
    pass

class EditCustomer(UpdateView):
    model = Customer
    template_name = 'user/register.html'
    form_class = CustomerForm
    success_url = reverse_lazy('user:list_user')

def deleteUser(request, id):
    pass


def listUser(request):
    query = request.GET.get('search')
    users = Customer.objects.all()
    if query:
        users = Customer.objects.filter(
            Q(first_name__icontains = query)|
            Q(dni__icontains = query)
        )
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'user/list.html',{"users":users})
    


'''class Login(FormView):
    template_name = 'login.html'
    form_class = LoginAdminForm
    

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
        
        def form_valid(self,form):
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)


class Home(TemplateView):
    template_name = 'user/home.html'

class ListUser(ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'
    queryset = User.objects.all()


class RegisterUser(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserForm
    success_url = reverse_lazy('user:list_user')


class EditUser(UpdateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserForm
    success_url = reverse_lazy('user:list_user')

def deleteUser(request, id):
    user = User.objects.get(id = id)
    user.delete()

    return redirect('user:list_user')


def listUser(request):
    query = request.GET.get('search')
    users = User.objects.all()
    if query:
        users = User.objects.filter(
            Q(first_name__icontains = query)|
            Q(dni__icontains = query)
        )
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'user/list.html',{"users":users})

'''

'''def editUser(request, id):
    user_form = None
    error = None
    try:
        user = User.objects.get(id = id)
        if request.method == 'GET':
            user_form = UserForm(instance = user)
        else:
            user_form = UserForm(request.POST, instance = user)
            if user_form.is_valid():
                user_form.save()
                return redirect('user:list_user')
        
    except ObjectDoesNotExist as identifier:
        error = identifier
    
    return render(request, 'user/register.html', {'user_form':user_form,'error':error})
'''
'''def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:list_user')
    else:
        user_form = UserForm()
    
    return render(request, 'user/register.html',{'user_form':user_form})
'''
from django.urls import path
from . import views

urlpatterns = [
    path('list',views.listUser, name='list_user'),
    path('register',views.RegisterUser.as_view(), name='register_user'),
    path('registercustomer',views.RegisterCustomer.as_view(), name='register_customer'),
    path('editcustomer/<int:pk>',views.EditCustomer.as_view(), name='edit_customer'),
    #path('edit/<int:id>', views.editUser, name='edit_user'),
    #path('edit/<int:pk>', views.EditUser.as_view(), name='edit_user'),
    path('delete/<int:id>', views.deleteUser, name='delete_user'),
]
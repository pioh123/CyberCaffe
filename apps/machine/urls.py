from django.urls import path
from . import views

urlpatterns = [
    path('list',views.ListMachine.as_view(), name='list_machine'),
    path('addMachine', views.AddMachine.as_view(), name='add_machine'),
    path('editMachine/<int:pk>', views.EditMachine.as_view(), name='edit_machine')

    
]
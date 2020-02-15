from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listp',views.listProduct, name='list_product'),
    path('add',views.AddProduct.as_view(), name='add_product'),
    path('edit/<int:pk>',views.EditProduct.as_view(),name='edit_product'),
    path('delete/<int:id>', views.deleteProduct,name='delete_product'),
    path('quantity',views.quantityProduct, name='quantity_product'),
    path('listAd',views.listAdvertise, name='list_advertise'),
    path('addAdvertise', views.addAdvertise, name="add_advertise"),
    path('editAdvertise/<int:pk>', views.EditAdvertise.as_view(), name="edit_advertise"),
    path('deleteAdvertise/<int:id>', views.deleteAdvertise, name= 'delete_advertise'),
    path('productoAPI',views.ProductListAPI.as_view(),name='product_list_API')
    
]


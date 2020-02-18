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
    path('productoAPI',views.ProductListAPI.as_view(),name='product_list_API'),
    path('advertiseAPI',views.AdvertiseListAPI.as_view(),name='advertise_list_API'),
    path('listPromotion',views.ListPromotion.as_view(),name='list_promotion'),
    path('addPromotion',views.AddPromotion.as_view(),name='add_promotion'),
    path('editPromotion/<int:pk>', views.EditPromotion.as_view(), name='edit_promotion'),
    path('promotionAPI',views.PromotionListAPI.as_view(),name='promotion_list_API'),
    
]


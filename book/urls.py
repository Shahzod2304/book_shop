from django.urls import path 
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add/<int:pk>/', AddProducts.as_view(), name='addproduct'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('news/<int:pk>/', NewsPageDetail.as_view(), name='news_detail'),
    path("add-to-cart-<int:pro_id>/",AddToCartView.as_view(),name="addtocart"),
    path("my-cart/", MyCartView.as_view(),name="mycart"),
    path('manage-cart/<int:cp_id>/',ManageCartView.as_view(),name='managecart'),
    path("empty-cart/",EmptyCartView.as_view(),name='emptycart'),
    path('aksiya/',AksiyaView.as_view(),name='aksiya')
    
]
from django.urls import path,include
# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('home', views.index,name="home"),
    path('shop/', views.shop,name="shop"),
    path('cart/', views.shop,name="cart"),
    # path('product/<pk>', views.product,name="product"),
    # path('add_review/', views.add_review, name='add_review'),
]
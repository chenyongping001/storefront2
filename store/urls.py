from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

route = routers.DefaultRouter()
route.register('products', views.ProductViewSet, basename='products')
route.register('collections', views.CollectionViewSet)
route.register('carts', views.CartViewSet)
product_routers = routers.NestedDefaultRouter(
    route, 'products', lookup='product')
product_routers.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
cart_routers = routers.NestedDefaultRouter(
    route, 'carts', lookup='cart')
cart_routers.register('items', views.CartItemViewSet,
                      basename='cart-items')
# URLConf
urlpatterns = route.urls+product_routers.urls+cart_routers.urls

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('get_all_images', views.getImages),
    path('products', views.ProductViewSet.as_view()),
    path('products/<pk>', views.ProductViewSet.as_view()),
    path('checkout', views.CartView.as_view()),
    path('upload_image/',views.APIViews.as_view()),
   ]

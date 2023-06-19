from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import  customerapiview,productapiview,productdetailapiview,customerdetailapiview,productviewset
from . import views

router=DefaultRouter()
router.register(r'products',productviewset)

urlpatterns=[
    path('api/customers/',customerapiview.as_view(),name = 'customerapiview'),
    path('api/customers/<int:pk>/',customerdetailapiview.as_view(),name='customerdetailapiview'),
    path('api/products/',productapiview.as_view(),name='productapiview'),
    path('api/products/<int:pk>/',productdetailapiview.as_view(),name='productdetailapiview'),
    path('api/',include(router.urls)),
    path('',views.index,name='index'),
    path('/products/',views.products,name='products'),

]
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

class customerapiview(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class customerdetailapiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer    

class productapiview(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer    

class productdetailapiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer   

class productviewset(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=ProductSerializer

    @action(detail=True,methods=['post'])
    def active_stat(self,request,pk=None):
        products=self.get_object()

        if products.registered_date():
            products.date=False
            product.save()
        return Response({'message':'updated'})

            
def index(request):
    customers=Customer.objects.all()
    return render(request,'customer.html',{'customers':customers}) 

def products(request):
    productss=product.objects.all()
    return render(request,'prod.html',{'productss':productss})
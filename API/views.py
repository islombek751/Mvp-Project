from django.contrib.auth import models
from django.db.models.query_utils import PathInfo
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
import datetime
from API.models import Client, Driver, Order
from .serializer import OrderSerializer, RegisterSerializer, UserSerializer
from django.contrib.auth.models import User

# User registration
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

# It receivies driver's id and client's id.
# And It creates order, then returns the order's 'id'.
class CreateOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        driver = get_object_or_404(Driver,id=int(request.POST['driver'])) 
        client = get_object_or_404(Client,id=int(request.POST['client']))
        order = Order.objects.create(driver=driver,client=client)
        serializer = OrderSerializer(order,read_only=True)
        return Response({"Order id":f"{serializer.data['id']}","status":f"{serializer.data['status']}"})

# Here,the order's status which you send 'id' can be updated!
class UpdateOrder(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def put(self,request):
        order = get_object_or_404(Order,id=int(request.POST['id'])) 
        status = request.POST['status']
        if order.status == "accepted" and status == "cancelled":
            return Response({"Repsonse":"Accepted order can not be cancelled!"})
        else:
            order.status=status; order.save()
            serializer = OrderSerializer(order,read_only=True)
            return Response({"Response":f"{serializer.data['status']}"})


# Here I send all of the client's orders. 
# If you add additional parameters, it returns filtered informations!
class ClientsOrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        client = get_object_or_404(Client,id=self.kwargs['client_id'])
        if 'from' in self.request.GET and 'to' in self.request.GET:
            info1 = self.request.GET['from']
            info2 = self.request.GET['to']
            froo = (str(info1).split('/'))
            to = (str(info2).split('/'))
            date1 = datetime.datetime(int(froo[2]),int(froo[1]),int(froo[0]))
            date2 = datetime.datetime(int(to[2]),int(to[1]),int(to[0]))
            queryset = Order.objects.filter(client=client,updated_time__range=(date1, date2))
            return super().filter_queryset(queryset)
        else:
            queryset = Order.objects.filter(client=client)
            return super().filter_queryset(queryset)
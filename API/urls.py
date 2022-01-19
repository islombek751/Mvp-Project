from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
      path('register', RegisterApi.as_view()),#Get
      path('create', CreateOrder.as_view()),#Post
      path('update_status', UpdateOrder.as_view()),#Put
      # http://127.0.0.1:8000/api/orders/client/1?from=5/01/2022&to=12/01/2022 <<< url maybe like this
      path('orders/client/<int:client_id>/', ClientsOrderList.as_view()),#Get

]
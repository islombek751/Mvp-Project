from django.db import models
from django.db.models.enums import Choices
from django.contrib.auth.models import User
# Create your models here.
class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    #etc...
    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    #etc...
    def __str__(self):
        return self.name

class Order(models.Model):
    conditions = (
        ('created','created'),
        ('cancelled',"cancelled"), 
        ("accepted", "accepted"),
        ("finished", "finished"),
    )
    driver  = models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True)
    client  = models.ForeignKey(Client,on_delete=models.CASCADE)
    status = models.CharField(max_length=35,choices=conditions,default='created')
    created_time = models.DateField(auto_now_add=True)   
    updated_time = models.DateTimeField(auto_now=True)   


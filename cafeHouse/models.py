from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    title=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=500,null=True)
    ingredients=models.TextField(max_length=300,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(null=True)
    day=models.IntegerField(null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    note=models.TextField(max_length=500,null=True)

class Company_Details(models.Model):
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    fb=models.TextField(max_length=100,null=True)
    instagram = models.TextField(max_length=100, null=True)
    twitter = models.TextField(max_length=100, null=True)
    youtube = models.TextField(max_length=100, null=True)
    linkedIn = models.TextField(max_length=100, null=True)

class Contact_Data(models.Model):
    name=models.TextField(max_length=20,null=True)
    email=models.EmailField(max_length=100,null=True)
    subject=models.TextField(max_length=200,null=True)
    message=models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name


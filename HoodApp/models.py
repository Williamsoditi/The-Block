from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

# Neighbourhood model
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=20,blank=True,null=True,unique=True)
    hood_image = CloudinaryField('hood_image',null=True)
    description = models.TextField(null=True,max_length=200)
    resident_count = models.IntegerField(default=0)
    admin = models.ForeignKey('Profile', on_delete=models.CASCADE,null=True,related_name='hood')
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    help_line = models.CharField(max_length=20,null=True)

    
    def __str__(self):
        return self.hood_name

    def create_neighbourhood(self):
        self.save()

    def update_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def find_neighbourhood(cls,neighbourhood_id):
        hood = cls.objects.filter(neighbourhood_id=neighbourhood_id)
        return hood

#LOCATION
class Location(models.Model):
    name = models.CharField(max_length=20,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



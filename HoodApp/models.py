from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

#PROFILE 
class Profile(models.Model):
    prof_photo = CloudinaryField('image')
    bio = models.TextField(max_length=1000, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='profile')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


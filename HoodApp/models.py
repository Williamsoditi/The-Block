from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

#BUSINESS
class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_logo = CloudinaryField('logo')
    business_contact = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def update_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

    @classmethod
    def get_business(cls,id):
        business = Business.objects.filter(neighbourhood__pk = id)
        return business


#PROFILE 
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
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

# POST
class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_post(cls, hood):
        post = Post.objects.filter(hood=hood)
        return post

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


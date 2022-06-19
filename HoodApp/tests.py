from django.test import TestCase
from .models import *

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.komarocks = Location(name='Location',updated_on='19/06/2022',created_on='15/06/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.komarocks, Location))

    def test_save_method(self):
        self.komarocks.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.komarocks.save_location()
        self.komarocks.delete()
        locations = Location.objects.all()
        self.assertFalse(len(locations) > 0)

    def tearDown(self):
        Location.objects.all().delete()

class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(title='Test Post',description='Nice hood')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save()
        self.post.delete_post()
        posts = Post.objects.all()
        self.assertFalse(len(posts) > 0)

    def test_get_post(self):
        user = 1
        post = Post.get_post(user)
        self.assertFalse(len(post)>0)
    
    def tearDown(self):
        Post.objects.all().delete()

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business1 = Business(business_name='Test Business',business_logo='logo.png',business_contact='test@test.com',created_at='19/06/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.business1, Business))

    def test_create_method(self):
        self.business1.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business1.save()
        self.business1.delete_business()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)

    def tearDown(self):
        Business.objects.all().delete()

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.hood1 = Neighbourhood(hood_name='Test Business',hood_image='logo.png',help_line='test@test.com',created_on='12/06/2022',updated_on='16/06/2022',description='Test hood',resident_count='5')

    def test_instance(self):
        self.assertTrue(isinstance(self.hood1, Neighbourhood))

    def test_create_method(self):
        self.hood1.save()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)
    
    def test_delete_method(self):
        self.hood1.save()
        self.hood1.delete_neighbourhood()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)
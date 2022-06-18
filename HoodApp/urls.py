from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
]
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/', views.profile,name='profile'),
    path('accounts/profile/', views.home,name='profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile,name='update_profile'),
    path('create_hood/',views.create_hood,name = 'create_hood'),
    path('hoods',views.hoods,name='hoods'),
    path('hood/<int:id>',views.specific_hood,name='specific_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>',views.leave_hood,name='leave_hood'),
    path('create_business/',views.create_business,name = 'create_business'),
    path('create_post/',views.create_post,name = 'create_post'),
    path('search/', views.search, name='search'),
]
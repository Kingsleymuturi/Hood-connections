from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('', views.hoods, name='hoods'),
    path('new-hood/', views.create_hood, name='new-hood'),
]
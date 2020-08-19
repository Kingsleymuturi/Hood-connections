from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('', views.index, name='index'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
]
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('<hood_id>/new-post', views.create_post, name='post'),
]
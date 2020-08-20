from django.urls import path
from hoodie.api.views import(
    registration_view,
    hoods,
    view_hood,    
    create_hood,
    update_hood,
    delete_hood,
) 
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'hoodie'

urlpatterns = [
    path('v1/create_hood/', create_hood, name='create-hood'),
    path('v1/hoods/<int:pk>/update_hood/', update_hood, name='update-hood'),
    path('v1/hoods/<int:pk>/delete_hood/', delete_hood, name='delete-update'),
    path('v1/hoods/', hoods, name='hoods'),
    path('view_hood/', view_hood, name='hood_info'),
    path('auth/register/', registration_view, name='register'),
    path('auth/login/',obtain_auth_token, name='login'),
]
from rest_framework import serializers
from hoodie.models import NeighbourHood
from django.contrib.auth.models import User

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ['admin','name','location','description','hood_logo','health_tell','police_number']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def save(self):
        account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account
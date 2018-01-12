from rest_framework import serializers
from principal.models import Usuario
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email',  'age')
        def create(self, validated_data):
            return Usuario.objects.create(**validated_data)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('result','msg','role')
        
        def create(self, validated_data):

            return Usuario.objects.create(**validated_data)
        
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('result','msg')
        
        def create(self, validated_data):

            return Usuario.objects.create(**validated_data)        
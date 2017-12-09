from django.forms import widgets
from rest_framework import serializers
from principal.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'email', 'genre', 'autonomous_community', 'age', 'role')
        
        def create(self, validated_data):

            return User.objects.create(**validated_data)
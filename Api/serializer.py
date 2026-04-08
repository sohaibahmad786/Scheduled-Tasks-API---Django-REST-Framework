from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

from .models import Register
from .models import Task

class Register_serializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','password']
        
    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)


class Task_serializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

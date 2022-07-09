from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField()
    
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('Username', instance.username)
    #     instance.first_name = validated_data.get('First Name',instance.first_name)
    #     instance.last_name = validated_data.get('Last Name', instance.last_name)
    #     instance.email = validated_data.get('Email Address', instance.email)
    #     instance.save()
    #     return instance
# class CustomUserDetailSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = instance.password
        instance.save()
        return instance


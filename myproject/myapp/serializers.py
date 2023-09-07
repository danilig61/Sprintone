from rest_framework import serializers
from .models import Pass , Photo

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['coordinates', 'height', 'name', 'user_name', 'user_email', 'user_phone']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']
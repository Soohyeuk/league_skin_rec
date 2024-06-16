from rest_framework import serializers
from .models import Users

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'created_at', 'password']
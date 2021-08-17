from rest_framework import serializers
from .models import User

class UserSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'last_name',
            'email',
            'is_staff',
            'is_superuser'
        )

class UserSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'last_name',
            'email',
            'password',
            'is_staff',
            'is_superuser'
        )
    
    def create(self, validated_data):
        user = User(**validated_data)
        print('Password:', validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
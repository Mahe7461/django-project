from rest_framework import serializers
from .models import em

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = em
        fields = ('id','username','Email_ID')
        

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = em
        fields = ('id', 'username', 'Email_ID', 'password')


        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = em(validated_data['Email_ID'], validated_data['username'], validated_data['password'])

        return user
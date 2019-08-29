from rest_framework import serializers
from .models import UserProfile
from django.db.models import Avg
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','first_name','last_name','email')


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        depth = 1
        exclude=('user_type','id')

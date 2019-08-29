from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import StudentProfileSerializer
from .models import  UserProfile
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views #to extend AuthToken for sending first name and last name along with token
#from django.conf import settings
from rest_framework.response import Response

class AuthToken(views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,'first_name':user.first_name,'last_name':user.last_name})

class FetchStudentProfile(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentProfileSerializer
    def get_queryset(self):
        return UserProfile.objects.all()

    def get_object(self):
      queryset = self.get_queryset()
      obj = get_object_or_404(queryset, user=self.request.user)
      return obj

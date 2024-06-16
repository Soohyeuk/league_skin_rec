from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Users 
from .serializers import UserSerializers



class UserView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    #permission_classes = [IsAuthenticated]

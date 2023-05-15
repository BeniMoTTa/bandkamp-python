from rest_framework import generics
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated


class UserView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner, IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(APIView):
    def get(self, request):
        if request.user.is_superuser:
            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            return user
        except CustomUser.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        if request.user == CustomUser.objects.get(pk=pk):
            user = self.get_object(pk)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        return Response({"Oops, you're trying to look at another user's details again. Please go to your user profile."}, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk):
        if request.user_id == self.get_object(pk):
            serializer = CustomUserSerializer(request.user_id, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"Oops! You're changing your user information to something strange. Give it another go."}, status=status.HTTP_400_BAD_REQUEST)

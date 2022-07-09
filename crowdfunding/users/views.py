from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer

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
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        if request.user == self.get_object(pk):
            serializer = CustomUserSerializer(request.user)
            return Response(serializer.data)
        return Response({"Oops! You're trying to look at another user's details. Please go to your user profile."}, status=status.HTTP_401_UNAUTHORIZED)

    # def put(self, request, pk):
    #     if request.user == self.get_object(pk):
    #         user = self.get_object(pk)
    #         data = request.data
    #         serializer = CustomUserDetailSerializer(instance=user, data=data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #         return Response(serializer.errors, {"Oops! You're changing your user information to something strange. Give it another go."}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(instance=user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
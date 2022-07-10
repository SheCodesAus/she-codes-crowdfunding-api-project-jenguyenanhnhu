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
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
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

    def put(self, request, pk):
        if request.user == self.get_object(pk): 
            serializer = CustomUserSerializer(instance=self.get_object(pk), data=request.data, partial=True)
            if serializer.is_valid():  
                serializer.save()
                return Response(serializer.data, {"Your details have been updated"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, {"Oops! We don't need those details from you. Try updating your first name, last name, email address, or username again."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, {"Oops! You're trying to edit another user's details. Please go to your user profile."}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        if request.user == self.get_object(pk):
            serializer = CustomUserSerializer(request.user)
            serializer.delete()
            return Response(serializer.data, {"You've just deleted your account."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, {"Oops! You can only delete your user account. Go to your account to do so."}, status=status.HTTP_401_UNAUTHORIZED)
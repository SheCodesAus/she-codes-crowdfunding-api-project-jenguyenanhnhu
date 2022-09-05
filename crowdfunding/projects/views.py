from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Post
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PostSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_project(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = ProjectDetailSerializer(self.get_project(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ProjectDetailSerializer(instance=self.get_project(pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, {"Oops! You didn't create this project. Try editing your own project."}, status=status.HTTP_401_UNAUTHORIZED)

class PostList(APIView):
    
    def get(self, request, pk):
        serializer = PostSerializer(data=request.data)
        return Response(serializer.data)


class PostDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_post(self, pk):
        try:
            post = post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request):
        serializer = PostSerializer(data=request.data)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = PostSerializer(instance=self.get_post(pk), data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, {"Yippee! You've now updated your supporters with your progress."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, {"Oops! Try updating your support network again."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        serializer = PostSerializer(instance=self.get_post(pk), data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, {"Yippee! You've now updated your supporters with your progress."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, {"Oops! Try updating your support network again."}, status=status.HTTP_400_BAD_REQUEST)

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if request.user.is_anonymous == True:
            return Response({"Oops! You need to be logged in to give to a project."}, status=status.HTTP_401_UNAUTHORIZED)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PledgeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        serializer = PledgeSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = PledgeSerializer(instance=self.get_object(pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, {"Oops! You're trying to change someone else's pledge."}, status=status.HTTP_401_UNAUTHORIZED)

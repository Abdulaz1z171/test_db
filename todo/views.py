from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



# Create your views here.

class PostListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    
    filterset_fields = ['created']
    search_fields = ['title']
    order_fields = ['updated']

    
class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
from django.shortcuts import render
from .models import BlogPosts
from .serializer import BlogPostSerializer
from rest_framework import generics

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
  queryset = BlogPosts.objects.all()
  serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPosts.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = 'pk'

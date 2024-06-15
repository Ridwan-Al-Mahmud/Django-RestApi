from rest_framework import serializers
from .models import BlogPosts

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPosts
    fields = ['id', 'title', 'content', 'published_data']
    
from rest_framework import serializers
from .models import BlogPost  # Import your BlogPost model

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'  # Or specify the fields  want to include

from rest_framework import serializers
from .models import ImageItem

class ImageItemSerializer(serializers.ModelSerializer):
    image_file = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = ImageItem
        fields = ['id', 'title', 'description', 'image_url', 'cloudinary_public_id', 'uploaded_at', 'image_file']
        read_only_fields = ['image_url', 'cloudinary_public_id', 'uploaded_at']

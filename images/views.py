from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ImageItem
from .serializers import ImageItemSerializer
from .services import upload_image_to_cloudinary

class ImageItemViewSet(viewsets.ModelViewSet):
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_file = serializer.validated_data.pop('image_file')
        image_url, public_id = upload_image_to_cloudinary(image_file)

        image_item = ImageItem.objects.create(
            image_url=image_url,
            cloudinary_public_id=public_id,
            **serializer.validated_data
        )

        return Response(ImageItemSerializer(image_item).data, status=status.HTTP_201_CREATED)

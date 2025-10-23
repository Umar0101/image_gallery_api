from django.contrib import admin
from .models import ImageItem
from .forms import ImageItemAdminForm

class ImageItemAdmin(admin.ModelAdmin):
    form = ImageItemAdminForm
    list_display = ('title', 'description', 'image_url', 'cloudinary_public_id', 'uploaded_at')

admin.site.register(ImageItem, ImageItemAdmin)

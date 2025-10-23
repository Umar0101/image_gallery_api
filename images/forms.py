from django import forms
from .models import ImageItem

class ImageItemAdminForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = ImageItem
        fields = ['title', 'description', 'image_file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            import cloudinary.uploader
            result = cloudinary.uploader.upload(image_file)
            instance.image_url = result.get('secure_url')
            instance.cloudinary_public_id = result.get('public_id')

        if commit:
            instance.save()
        return instance

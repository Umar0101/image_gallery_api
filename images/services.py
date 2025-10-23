import cloudinary.uploader

def upload_image_to_cloudinary(file):
    result = cloudinary.uploader.upload(file)
    return result.get('secure_url'), result.get('public_id')

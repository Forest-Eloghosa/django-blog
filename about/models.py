from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
     """
    Stores a single about me text
     """
     title = models.CharField(max_length=200)
     profile_image = CloudinaryField('image', default='placeholder')
     
     @property
     def image_url(self):
         """
         Return a safe URL for the about profile image.
         Falls back to a static default if the Cloudinary field isn't available
         or accessing `.url` raises an exception in production.
         """
         try:
             url = self.profile_image.url
             if url:
                 return url
         except Exception:
             pass

         from django.conf import settings
         return settings.STATIC_URL + 'images/nobody.jpg'
     updated_on = models.DateTimeField(auto_now=True)
     content = models.TextField()

     def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
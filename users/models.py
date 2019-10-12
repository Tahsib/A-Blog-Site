from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_img = models.ImageField(
        default='default.jpg', upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img1 = Image.open(self.pro_img.path)

        if img1.height > 300 or img1.width > 300:
            out1 = (300, 300)
            img1.thumbnail(out1)
            img1.save(self.pro_img.path)

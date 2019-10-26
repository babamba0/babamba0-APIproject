from django.db import models
## AUTH_USER_MODEL을 불러오기 위한 settings import
from django.conf import settings

# Create your models here.
class Essay(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()

## Album , Files 추가.
class Album(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)

class Files(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(blank=False,
                            null=False, upload_to="files")
    desc = models.CharField(max_length=100)
from django.db import models

# Create your models here.
class FileUpload(models.Model):
    title = models.CharField(default='', max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(null=True, blank=True)
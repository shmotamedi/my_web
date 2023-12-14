from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    is_enable=models.BooleanField(default=False)
    created_time=models.DateTimeField()
    updated_time=models.DateTimeField()

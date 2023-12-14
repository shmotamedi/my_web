from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField(blank=True,null=True)
    is_enable=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

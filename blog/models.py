from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
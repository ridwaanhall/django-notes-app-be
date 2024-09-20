from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    tags = models.JSONField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
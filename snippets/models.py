from django.db import models
from accounts.models import CustomUser


class Snippet(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=False)
    code = models.TextField()
    language = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title if self.title else f"Snippet by {self.author}"

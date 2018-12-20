from django.contrib.auth.models import User
from django.db import models


class Help(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)
    email = models.EmailField()



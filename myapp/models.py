from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobileNumber = models.CharField(max_length=15, null=True)
    regDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

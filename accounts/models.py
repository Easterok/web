from django.db import models
from django.contrib.auth.models import User
from boards.models import Board


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_avatar = models.ImageField(upload_to='profile_avatar/', default='profile_avatar/default.png', blank=False)
    birthday = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    boards = models.ForeignKey(Board, on_delete=models.CASCADE, default=0)

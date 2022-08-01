from django.db import models
from django.contrib.auth.models import User

class MusicPost(models.Model):
    likes = models.ManyToManyField(User, related_name='musicpost_like')

    def number_of_likes(self):
        return self.likes.count()
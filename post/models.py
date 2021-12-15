from django.conf import settings
from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Like(models.Model):
    like_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like_user', on_delete=models.CASCADE)
    like_post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE, null=True)
    like = models.PositiveSmallIntegerField(default=0)
    like_published = models.DateTimeField(auto_now_add=True)


class Dislike(models.Model):
    dislike_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dislike_user', on_delete=models.CASCADE)
    dislike_post = models.ForeignKey(Post, related_name='dislike_post', on_delete=models.CASCADE)
    dislike = models.PositiveSmallIntegerField(default=0)
    dislike_published = models.DateTimeField(auto_now_add=True)
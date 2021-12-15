from rest_framework import serializers

from authentication.models import User
from .models import Post, Like, Dislike


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'last_login']


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_login']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['like_user', 'like_post', 'like', 'like_published']


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['dislike_user', 'dislike_post', 'dislike', 'dislike_published']

import json

from django.http import HttpResponse
from rest_framework import generics, permissions, status, viewsets

from authentication.models import User

from .models import Post, Like, Dislike
from post.serializers import PostSerializer, PostCreateSerializer, LikeSerializer, DislikeSerializer, UserSerializer, \
    UserActivitySerializer
from .pagination import PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PostPageNumberPagination


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer


class PostLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class PostDislikeView(generics.CreateAPIView):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer


class PostAnaliticsLikesView(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        likes_analitic = Like.objects.filter(like_published__range=[kwargs['date_from'], kwargs['date_to']])
        if len(likes_analitic) > 0:
            mimetype = 'application/json'
            return HttpResponse(json.dumps({'likes by period': len(likes_analitic)}), mimetype)
        else:
            return self.list(request, *args, [{}])

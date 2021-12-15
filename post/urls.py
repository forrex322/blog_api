from django.urls import path

from post import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('user_activity/<int:pk>/', views.ActivityUserView.as_view(), name='user_activity'),
    path('posts/', views.PostList.as_view()),
    path('posts/create/', views.PostCreateAPIView.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdateAPIView.as_view()),
    path('posts/<int:post_pk>/<int:user_pk>/like', views.PostLikeView.as_view(), name='post_like'),
    path('posts/<int:post_pk>/<int:user_pk>/dislike/', views.PostDislikeView.as_view(), name='post_dislike'),
    path('posts/analitics/date_from=<date_from>&date_to=<date_to>/', views.PostAnaliticsLikesView.as_view(),
         name='post_likes'),
]

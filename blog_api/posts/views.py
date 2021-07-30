from django.contrib.auth import get_user_model
from rest_framework import viewsets

from rest_framework import generics, permissions
from .models import Post, Comment

from .serializers import PostSerializer, UserSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly, IsNameOrReadOnly


from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.urls import reverse
from rest_auth.registration.views import SocialLoginView

import urllib.parse

from django.shortcuts import redirect


# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# or
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
# or

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsNameOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GitHubLogin(SocialLoginView):
    adapter_class = github_views.GitHubOAuth2Adapter
    client_class = OAuth2Client
    # callback_url = 'http://127.0.0.1:8000/auth/github/login/callback'  # Django-allauth

    @property
    def callback_url(self):
        # use the same callback url as defined in your GitHub app, this url
        # must be absolute:
        return self.request.build_absolute_uri(reverse('github_callback'))


def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://127.0.0.1:8000/auth/github?{params}')

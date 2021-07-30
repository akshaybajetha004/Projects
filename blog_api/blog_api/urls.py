"""blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from allauth.socialaccount.providers.github import views as github_views

from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.urls import reverse
from rest_auth.registration.views import SocialLoginView

import urllib.parse

from django.shortcuts import redirect

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_swagger_view(title=API_TITLE)


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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger-docs/', schema_view),

    path('auth/', include('rest_auth.urls')),
    path('auth/github', GitHubLogin.as_view()),
    path('auth/github/callback/', github_callback, name='github_callback'),
    path('auth/github/url/', github_views.oauth2_login)

]

from django.urls import path
# from .views import PostList, PostDetail,  UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet, CommentViewSet

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
urlpatterns = router.urls

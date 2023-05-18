from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='token_auth'),
    path('v1/', include(router.urls)),
]

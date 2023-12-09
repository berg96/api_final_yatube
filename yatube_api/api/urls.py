from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'
router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)
router_v1.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]

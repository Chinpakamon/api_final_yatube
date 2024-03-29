from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='Post')
v1_router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment')
v1_router.register('groups', GroupViewSet, basename='Group')
v1_router.register('follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

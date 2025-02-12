from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostList, PostDetail, UserDetail
from rest_framework.authtoken import views

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("users/<int:pk>/", UserDetail.as_view(), name="api_user_detail"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from .views import register, user_login, user_logout, profile
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, search_posts
from taggit.views import tagged_object_list
from .models import Post

urlpatterns = [
    # Authentication urls
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),

    # Blog post urls
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments view urls
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    # Searcg view urls
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', tagged_object_list, {'queryset': Post.objects.all(), 'template_name': 'blog/tagged_posts.html'}, name='posts_by_tag'),
]

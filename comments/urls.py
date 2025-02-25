from django.urls import path
from . import views


urlpatterns = [
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment_list'),
]
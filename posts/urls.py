from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

]
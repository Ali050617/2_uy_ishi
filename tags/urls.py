from django.urls import path
from . import views


urlpatterns = [
    path('tags/', views.TagListCreateView.as_view(), name='tag_list'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
]
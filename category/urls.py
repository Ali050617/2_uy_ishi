from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.CategoryListCreateView.as_view(), name='list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='detail')
]
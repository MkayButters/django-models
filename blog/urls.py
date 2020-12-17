from django.urls import path
from .views import HomeView, BlogDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
]

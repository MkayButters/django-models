from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
    template_name = "home.html"
    model = Post

class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

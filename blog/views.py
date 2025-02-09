from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()) # This will get all the posts from the database
    return render(request, 'blog/index.html', {'posts': posts}) # This will render the index.html template

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post":post})
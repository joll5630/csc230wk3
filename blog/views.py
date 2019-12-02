from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-created_date')[:3]
    output = ' '.join([p.title for p in post_list])
    return render(request, 'bloghome.html',{'posts':post_list})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.db.models import Q
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    search_query = request.GET.get('q', '')
    
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'blog/home.html', {
        'form': form,
        'posts': posts,
        'search_query': search_query,
    })

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.liked = not post.liked
        post.save()
        return JsonResponse({'liked': post.liked})
    return JsonResponse({'error': 'Invalid request'}, status=400)
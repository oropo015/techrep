from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category

def home(request):
    published_posts = Post.objects.filter(is_published=True)
    featured_posts = published_posts.filter(is_featured=True)[:3]
    latest_posts = published_posts[:12]
    categories = Category.objects.all()[:6]
    
    context = {
        'featured_posts': featured_posts,
        'latest_posts': latest_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    post.views += 1
    post.save(update_fields=['views'])
    
    related_posts = Post.objects.filter(
        category=post.category,
        is_published=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, is_published=True)
    
    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'blog/category.html', context)

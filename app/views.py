from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Trend
from django.contrib import messages
from .forms import ContactForm
from django.core.paginator import Paginator
from django.db.models import Q, F, Value, CharField
from django.db.models.functions import Concat
from django.contrib.auth.models import User

def home(request):
    # Fetch published posts and trends
    posts = Post.objects.filter(published=True).order_by('-created_at')[:7]
    trends = Trend.objects.filter(published=True).order_by('-created_at')[:5]

    # Fetch the latest published Post and Trend
    latest_post = Post.objects.filter(published=True).order_by('-created_at').first()
    latest_trend = Trend.objects.filter(published=True).order_by('-created_at').first()

    # Combine into trending_posts list
    trending_posts = []
    if latest_post:
        trending_posts.append({
            'id': latest_post.id,
            'title': latest_post.title,
            'author': latest_post.author,
            'url': 'post_detail'
        })
    if latest_trend:
        trending_posts.append({
            'id': latest_trend.id,
            'title': latest_trend.title,
            'author': latest_trend.author,
            'url': 'trend_detail'
        })

    context = {
        'trends': trends,
        'posts': posts,
        'trending_posts': trending_posts
    }
    return render(request, 'home.html', context)

def posts(request):
    # Get all published posts
    posts = Post.objects.filter(published=True).order_by('-created_at')

    # Pagination
    paginator = Paginator(posts, 4)  # Show 4 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Recent posts (last 5 published posts)
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:3]

    # Author info (use first user; adjust as needed)
    author = User.objects.first()  # Replace with specific author logic if needed

    context = {
        'posts': page_obj,
        'recent_posts': recent_posts,
        'author': author,
    }
    return render(request, 'posts.html', context)

def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(published=True) &
        (Q(title__icontains=query) | Q(content__icontains=query))
    ).order_by('-created_at')

    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Recent posts
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:5]

    # Author info
    author = User.objects.first()

    context = {
        'posts': page_obj,
        'recent_posts': recent_posts,
        'author': author,
    }
    return render(request, 'posts.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post
    }
    return render(request, "post_detail.html", context)

def trend_detail(request, id):
    post = get_object_or_404(Trend, id=id)

    context = {
        "post": post
    }
    return render(request, "post_detail.html", context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category, Tag
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
#from mysite.core.forms import SignupForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
	post=get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', {'post': post}) 

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', slug=post.slug)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', slug=post.slug)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			post = form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate (username=username, password=raw_password)
			login(request, user)
			return redirect('blog:post_list')
	else:
		form = UserCreationForm()
	return render(request, 'blog/signup.html', {'form':form})

def logout(request):
	auth.logout(request)
	return render(request,'blog/logout.html')

def user_detail(request):
	if request.method == "GET":
		form = UserCreationForm(request.GET)
		if form.is_valid():
			username = form.request.get('username')
			raw_password = form.request.get('password1')
			return username
	else:
		form = UserCreationForm()
	return render(request, 'blog/user_detail.html', {'form' : form})

# View function to show post related to Tag

def tag_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tag_list.html', {'tags' : tags})

def tag_post_list(request, slug):
	tag = Tag.objects.get(slug=slug)
	posts = Post.objects.filter(tag=tag)
	context = { 'tag' : tag , 'posts' : posts }
	return render(request, 'blog/tag_post_list.html',  context )	

# View function to show post related to Category

def category_list(request):
	categorys = Category.objects.filter(updated_time__lte=timezone.now()).order_by('updated_time')
	return render(request, 'blog/category_list.html', {'categorys': categorys})

def category_post_list(request, slug):
	category = Category.objects.get(slug=slug)
	posts = Post.objects.filter(category=category).all()
	context = {'category' : category , 'posts' : posts}
	# print (context)
	return render(request, 'blog/category_post_list.html', context )	





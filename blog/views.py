from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
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
	print(slug)
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

# def login(request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			post = form.save()
# 			username = form.cleaned_data.get('username')
# 			raw_password = form.cleaned_data.get('password1')
# 			user = authenticate (username=username, password=raw_password)
# 			login(request, user)
# 			return redirect('blog:post_list')
# 	else:
# 		form = UserCreationForm()
# 	return render(request, 'blog/signup.html', {'form':form})


# def login(request):
# 	if request.user.is_authenticated:
# 		 return redirect('registration/login.html')

# 	if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password = request.POST.get('password')
# 			user = auth.authenticate(username=username, password=password)

# 			if user is not None:
# 				# correct username and password login the user
# 				auth.login(request, user)
# 				return redirect('registration/login.html')

# 			else:
# 				messages.error(request, 'Error wrong username/password')

# 	return render(request, 'blog/logout.html')
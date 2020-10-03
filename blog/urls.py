from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name ='post_new'),    
    path('category_list/<str:slug>/', views.category_post_list, name='category_post_list'),    
    path('tag_list/<str:slug>/' , views.tag_post_list, name='tag_post_list'),
    path('post/<str:slug>/', views.post_detail, name ='post_detail'),
    path('category_list/', views.category_list, name = 'category_list'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('tag_list/', views.tag_list, name = 'tag_list'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/',views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('', views.post_list, name = 'post_list'),

]
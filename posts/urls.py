from django.contrib import admin
from django.urls import path
from posts import views


urlpatterns = [ 
    path('', views.PostListView.as_view(), name='home'),
    path('news/', views.AiListView.as_view(), name='ai'),
    path('crypto/', views.CryptoListView.as_view(), name='crypto'),
    path('software/', views.SoftwareListView.as_view(), name='software'),
    path('tech/', views.TechListView.as_view(), name='tech'),
    path('about/', views. AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('edit/<int:pk>/', views.PostcontrolDetailView.as_view(), name='post_control'),
    path('control/', views.ControlListView.as_view(), name='control'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
]
from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.CreateBlogView.as_view(), name='create_blog'),
    path('list/', views.BlogListView.as_view(), name='blog_list'),
]

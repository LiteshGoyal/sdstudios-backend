from django.urls import path
from . import views
urlpatterns = [
    path('create',views.CrateBlogView.as_view()),
    path('list',views.ListBlogView.as_view()),
]

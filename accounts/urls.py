from django.urls import path
from . import views

urlpatterns = [
     path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('current-user/', views.current_user_view, name='current_user'),
    path('user/update/', views.UserUpdateView.as_view(), name='user-update'),
]
from django.urls import path

from .views import UserRegisterView, UserLoginView, user_logout

urlpatterns = [
  path('register/', UserRegisterView.as_view(), name='register'),
  path('login/', UserLoginView.as_view(), name='login'),
  path('logout/', user_logout, name='logout'),

]

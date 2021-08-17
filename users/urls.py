from . import views
from django.urls import path
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path(route='user/', view=views.UserListAPI.as_view(), name="Users"),
    path(route='user/<int:pk>/', view=views.UserDetailAPI.as_view(), name="User"),

    path(route='login/', view=views.login, name="Login"),
    path(route='token/', view=auth_views.obtain_auth_token, name="Token")
]

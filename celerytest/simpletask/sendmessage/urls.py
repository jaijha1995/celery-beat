from django.urls import path

from .views import *
from rest_framework.authtoken import views
from .views import *
from simpletask import settings

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('login/', Login.as_view()),
    path('registration/', RegisterView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('users/', UsersView.as_view()),
    path('message/', MessageView.as_view()),
    path('start-call/', StartCall.as_view()),
    path('end-call/', EndCall.as_view()),
    path('test-socket/', test_socket)
]

from django.urls import path
from .api import RegistrationAPI
from knox import views as knox_views
from .api import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('user/', UserAPI.as_view()),

]
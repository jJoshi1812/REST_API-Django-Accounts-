from django.urls import path,include,re_path
from . import views


urlpatterns = [
    path('login/', views.AuthToken.as_view()),
    path('profile/',views.FetchStudentProfile.as_view(),name='profile'),

    ]

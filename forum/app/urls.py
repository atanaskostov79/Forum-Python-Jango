from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('update-user/', views.updateUser, name="update-user"),


    path('', views.index, name='home'),
    path('question/<str:pk>', views.questionIndex, name='question'),
    path('questionlike/<str:pk>', views.questionLike, name='questionlike'),
    path('questiondislike/<str:pk>', views.questionDislike, name='questiondislike'),

    path('theme/<str:pk>', views.theme, name='theme'),


]
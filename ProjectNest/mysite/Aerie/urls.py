from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('welcome', views.welcome, name='welcome'),
    path('myNest', views.myNest, name='myNest'),
    path('findNest', views.findNest, name='findNest'),
    path('createNest', views.createNest, name='createNest'),

    path('api/createAccount', views.createAccountAPI, name='createAcountAPI'),
    path('api/createNest', views.createNestAPI, name='createNestAPI'),
    path('api/login', views.loginAPI, name='loginAPI'),
    path('api/myNest', views.myNestAPI, name='myNestAPI'),
    path('api/findNest', views.findNestAPI, name='findNestAPI')
]
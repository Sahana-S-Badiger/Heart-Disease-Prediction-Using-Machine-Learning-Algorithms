from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('predict/', views.predict, name='predict'),
    path('result/<str:result>/', views.result, name='result'),
    path('about/', views.about, name='about'),
]

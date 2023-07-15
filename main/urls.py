from django.urls import path
from . import views


urlpatterns = [
    path('testmain',views.home, name='main-home'),
    path('login/',views.log_in, name='main-login'),
    path('signup/',views.signup, name='main-signup'),
    path('booking/',views.booking, name='main-booking'),
    path('see_more_basic/',views.see_more_basic, name='main-see_more_basic'),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.testmain, name='testmain'),
]

from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),

    path('activate/uidb64/token/', views.activate, name='activate'),
    path('reset/uidb64/token/', views.reset, name='reset'),
    path('reset/<str:uidb64>/<str:token>/', views.reset, name='reset'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),


]

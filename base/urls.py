from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerUser, name='register'),

    path('logout/', views.logoutUser, name='logout'),
    path('', views.index, name='home'),

    path('profile/<str:pk>', views.userProfile, name='user-profile'),

    path('room/<str:pk>/', views.room, name='room'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),

    path('delete_comment/<str:pk>/', views.delete_comment, name='delete_comment'),
    path('update_profile/', views.UpdateProfile, name='update-profile'),
    path('topics/', views.TopicPages, name='topic'),
    path('activities/', views.ActivityPages, name='activity'),

]

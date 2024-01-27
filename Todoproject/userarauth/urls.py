from django.urls import path
from.import views

app_name='auth'
urlpatterns = [
    path('register/',views.registerUser,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),

    
    
]

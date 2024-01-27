from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('form/',views.Form,name='form'),
    path('details/<int:id>',views.Details,name='details'),
    path('update/<int:id>',views.Update,name='update'),
    path('delete/<int:id>',views.Delete,name='delete'),
]
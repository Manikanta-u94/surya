from django.urls import path
from . import views

urlpatterns = [

	path('',views.index,name='home'),

	path('add_post',views.add_post)
    
    
]
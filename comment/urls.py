
from django.urls import path
from  .views import  *

urlpatterns = [
    path('',update_comment,name='update_comment'),
]

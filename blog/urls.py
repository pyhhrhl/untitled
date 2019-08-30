
from django.urls import path
from  .views import  *

urlpatterns = [
    path('',blog_list,name='blog_list'),
    path('<int:blog_pk>',blog_detail,name = "blog_detail"),
    path('type/<int:blog_type_pk>',blog_with_type,name = "blog_with_type"),
    path('date/<int:year>/<int:month>',blog_with_date,name = "blog_with_date")
]

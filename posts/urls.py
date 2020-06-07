from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('/view/<int:post_id>', views.post_view, name='post_view'),
]

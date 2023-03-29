from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path("test/", views.test, name="test"),
    path("index/", views.index, name="index"),
    path('module/', views.module, name='module'),
    path("template/", views.template_view),
    path("home/", views.home_view),
    path("", views.blog_view),
    path("post/", views.blog_db),
    path("post/search/results/", views.results_view),
    path('post/delete/<int:id>', views.delete, name='delete'),
    path('post/search/', views.search),
    path("post/tag/<tag>", views.tag)
]
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('create', views.create_post, name='post_create'),
    path('list', views.post_list, name='post_list'),
    re_path(r'^view/(?P<pk>\d+)/$', views.post_view, name='view'),
    path('edit/<int:pk>/', views.post_edit, name='edit'),
    path('like/', views.post_like, name='post_like'),
    path('delete/<int:pk>/', views.post_delete, name='delete')
]
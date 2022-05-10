


from django.urls import path
from . import views
# from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.project, name='home'),
    path('about/<str:pk>/',views.about, name='about'),
    path('createPost',views.createPost,name='createPost'),
    path('updatePost/<str:pk>/',views.updatePost,name='updatePost'),
    path('deletePost/<str:pk>/',views.deletePost,name='deletePost'),

# for class view    
    # path('',PostListView.as_view(),name='home'),
    # path('about/<int:pk>',PostDetailView.as_view(),name='detail_post'),
]

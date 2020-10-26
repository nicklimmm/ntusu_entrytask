from django.urls import path
from .views import Home, PostDetailed, AddPost, EditPost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailed.as_view(), name='postdetailed'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('post/<int:pk>/edit/', EditPost.as_view(), name='editpost'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='deletepost')
    # path('login/', loginuser, name='login'),
    # path('register/', registeruser, name='register'),
]

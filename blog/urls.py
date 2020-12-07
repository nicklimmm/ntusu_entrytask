from django.urls import path
from .views import Home, PostDetailed, AddPost, EditPost, DeletePost, AddCategory, CategoryView, CategoryList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailed.as_view(), name='postdetailed'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('editpost/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('deletepost/<int:pk>/', DeletePost.as_view(), name='deletepost'),
    path('addcategory/', AddCategory.as_view(), name='addcategory'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryList, name='category-list'),
]

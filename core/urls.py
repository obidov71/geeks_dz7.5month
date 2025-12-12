from django.urls import path
from .import views
urlpatterns = [
    path('articles/',views.ArticleList.as_view(),name='article-list'),
    path('articles/<int:pk>/',views.ArticleDetail.as_view(),name='article-detail'),
    path('articles/<int:pk>/comments/',views.CommentList.as_view(),name='comment-list'),
    # path('articles/<int:pk>/comments/<int:comment_pk>/',views.CommentDetail.as_view(),name='comment-detail'),
]
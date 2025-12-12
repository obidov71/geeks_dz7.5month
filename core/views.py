from django.shortcuts import render
from rest_framework import generics
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['pk']
        return Comment.objects.filter(article__id=article_id)

    def perform_create(self, serializer):
        article_id = self.kwargs['pk']
        article = generics.get_object_or_404(Article, id=article_id)
        serializer.save(article=article)
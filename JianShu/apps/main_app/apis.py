from rest_framework import views, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
import logging

logger = logging.getLogger(__name__)
print __name__

class ArticleView(views.APIView):
    def get(self, request, pk=None):
        print 'bob flag, ', pk
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article, many=False)
            logger.debug('Get details of article "{}"'.format(article.title))
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            logger.debug('Get details of all articles')

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



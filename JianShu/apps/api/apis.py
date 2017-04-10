import logging

from django.shortcuts import get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response

from JianShu.apps.api.models import Article
from JianShu.apps.api.serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class ArticleView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
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
        data = dict(request.data)
        data['auth'] = request.user.pk
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        logger.debug('Illegal input, {}'.format(serializer.errors))
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

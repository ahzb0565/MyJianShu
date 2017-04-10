from rest_framework import serializers

from JianShu.apps.api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'auth', 'create_time', 'update_time')

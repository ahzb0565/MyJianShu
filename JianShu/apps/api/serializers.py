from rest_framework import serializers
from JianShu.apps.api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return '{} {}'.format(obj.auth.first_name, obj.auth.last_name)

    class Meta:
        model = Article
        fields = ('title', 'body', 'author', 'create_time', 'update_time')

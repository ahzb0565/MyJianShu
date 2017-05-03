import factory
from django.contrib.auth.models import User
from JianShu.apps.api.models import Article
from django.contrib.auth.hashers import make_password


user_password = 'password'

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'test_user_{}'.format(n))
    password = make_password(user_password)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = False


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Sequence(lambda n: 'Article {}'.format(n))
    body = factory.Sequence(lambda n: 'Article body {}'.format(n))
    auth = factory.SubFactory(UserFactory)

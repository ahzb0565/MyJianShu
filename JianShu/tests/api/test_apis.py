from JianShu.tests.factories import UserFactory, ArticleFactory, user_password
from django.test import TestCase
from django.core.urlresolvers import reverse


class ArticleViewTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()

    def tearDown(self):
        self.user.delete()

    def test_get(self):
        article = ArticleFactory.create(auth=self.user)
        assert self.client.login(username=self.user.username, password=user_password)
        response = self.client.get(reverse('api:article-details', kwargs={'pk': article.pk}))
        expect_response = {
            'body': u'Article body 0',
            'author': self.user.first_name + ' ' + self.user.last_name,
            'title': u'Article 0'}
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(expect_response, response.data.get('data'))

    def test_get_unauthenticated(self):
        article = ArticleFactory.create()
        response = self.client.get(reverse('api:article-details', kwargs={'pk': article.pk}))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.data.get('detail'),
            'Authentication credentials were not provided.'
        )

    def test_post(self):
        pass

    def test_post_unauthenticated(self):
        pass

from django.test import TestCase
from post.models import Post


class AccountTest(TestCase):

    def setUp(self):
        Post.objects.create(title='title1',  body='body1')
        Post.objects.create(title='title2',  body='body2')

    def test_user_create(self):
        p = Post.objects.filter(title='title1')
        self.assertEqual(p.count(), 1)


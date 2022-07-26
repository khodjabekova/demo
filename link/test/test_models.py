from django.test import TestCase
from link.models import UsefulLink


class AccountTest(TestCase):

    def setUp(self):
        UsefulLink.objects.create(link='https://docs.docker.com/engine/install/ubuntu/',  description='description1')
        UsefulLink.objects.create(link='https://hub.docker.com/_/ubuntu',  description='description2')

    def test_user_create(self):
        p = UsefulLink.objects.filter(link='https://docs.docker.com/engine/install/ubuntu/')
        self.assertEqual(p.count(), 1)


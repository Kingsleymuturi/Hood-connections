from django.test import TestCase
from .models import *


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Sindet', password='password')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class NeighbourHoodTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Sindet', password='password')
        self.admin = Profile.objects.create(id=1, name='name',location='location',user=self.user,bio='bio',neighbourhood=self.neighbourhood)
        self.neighbourhood = NeighbourHood.objects.create(id=1,name='name',location='location',admin=self.admin,description='des',health_tell=1234567,police_number=1234567)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, NeighbourHood))

    def test_create_neighbourhood(self):
        self.neighbourhood.create_neighborhood()
        neighbourHood = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourHood) > 0)

    def test_search_neighbourhood(self):
        self.neighbourhood.save()
        neighbourHood = NeighbourHood.find_neighborhood('name')
        self.assertTrue(len(neighbourHood) > 0)

    def test_delete_hood(self):
        self.neighbourhood.delete_neighborhood()
        neighbourHood = NeighbourHood.find_neighborhood('test')
        self.assertTrue(len(neighbourHood) < 1)

class BusinessTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Sindet', password='password')
        self.admin = Profile.objects.create(id=1, name='name',location='location',user=self.user,bio='bio',neighbourhood=self.neighbourhood)
        self.neighbourhood = NeighbourHood.objects.create(id=1,name='name',location='location',admin=self.admin,description='des',health_tell=1234567,police_number=1234567)
        self.business = Business.objects.create(id=1,name='name',description='des',user=self.user,neighbourhood=self.neighbourhood,email='algun@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_create_business(self):
        self.business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_search_business(self):
        self.business.save()
        business = NeighbourHood.search_business('name')
        self.assertTrue(len(business) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        business = business.search_business('name')
        self.assertTrue(len(business) < 1)

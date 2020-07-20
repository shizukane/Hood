from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestNeighbourhoodModel(TestCase):
  '''
  test class for  the neighbour model
  '''
  def setUp(self):
        '''
    the startup class of the class
    '''
    self.new_user = User(username = 'Liz')
    self.new_user.save()
    self.new_neighbourhood = Neighborhood(name = 'Ayany-court',location = 'KIbera',occupants = '22', image='hood.jpg', datecreated = '2019-10-30', health_department_contact='0700112233',police_authority_contact='0790234565',user = self.new_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_neighbourhood,Neighborhood))

  def test_create_neighbourhood(self):
    self.new_neighbourhood.save_neighborhood()
    neighborhoods = Neighborhood.objects.all()
    self.assertTrue(len(neighborhoods) > 0)


  def test_delete_neighbourhood(self):
    self.new_neighbourhood.save_neighborhood()
    self.new_neighbourhood.delete_neighborhood()
    neighborhoods = Neighborhood.objects.all()
    self.assertEqual(len(neighborhoods),0)



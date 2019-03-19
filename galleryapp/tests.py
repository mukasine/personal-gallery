from django.test import TestCase
from .models import Image, Location, categories

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = Location(id = 1,name = 'Gasabo')

    #Testing instance
  def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))  
    #testing the save method
    def save_save_method(self):
        self.james.save_location()
        self.Gasabo.save_location()
        self.assertTrue(len(locations) > 0)

    def test_update_method(self):
        self.location.save_location()
        self.location = Location.objects.filter(name = 'Gasabo').update(name = 'Kigali')
        self.updated_location = Location.objects.get(name = 'Kigali')
        self.assertEqual(self.updated_location.name,"Kigali")

    def test_delete_method(self):
        self.location.save_location()
        self.location = Location.objects.get(id = 1)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)


class CategoriesTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category = categories(id = 1,name = 'test')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,categories))

    #Testing Save method
    def test_save_method(self):
        self.category.save_category()
        self.categories = categories.objects.all()
        self.assertTrue(len(self.categories) > 0)

    def test_update_method(self):
        self.category.save_category()
        self.category = categories.objects.filter(name = 'test').update(name = 'changed')
        self.updated_category = categories.objects.get(name = 'changed')
        self.assertEqual(self.updated_category.name,"changed")

    def test_delete_method(self):
        self.category.save_category()
        self.category = categories.objects.get(id = 1)
        self.category.delete_category()
        self.assertTrue(len(categories.objects.all()) == 0)

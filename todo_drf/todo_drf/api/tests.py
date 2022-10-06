from .models import Task
from django.contrib.auth.models import User
from django.test import TestCase

class UnitModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):

        # Task Model
        Task.objects.create(id=3, title="install DRF" ,completed=1)

        # User Model
        User.objects.create(id=2, username="kanika")

        
    
    def test(self):
   
        user1=User.objects.get(id=2)
        self.assertEqual(user1.username, "kanika")

        Task1=Task.objects.get(id=3)
        self.assertEqual(Task1.title, "install DRF")
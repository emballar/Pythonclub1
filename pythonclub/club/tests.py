from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(title='The First Meeting')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'The First Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(title='Valorant Tournament')
        self.user=User(username= 'Erin')
        self.details= Event(title=self.type, location = 'Discord', user=self.user, date=datetime.date(2022,5,30), time='10:00pm', price=50.00, description="valorant tournament")

    def test_string(self):
        self.assertEqual(str(self.type), 'Valorant Tournament')

    def test_discount(self):
        disc = self.details.price * .05
        self.assertEqual(self.details.discountAmount(), disc)
    
    def test_discountAmount(self):
        self.assertEqual(self.details.discountPrice(), 47.5 )


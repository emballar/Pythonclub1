from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm
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
        disc = self.details.price * (1  - .05)
        self.assertEqual(self.details.discountPrice(), disc)

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data={
            'title':'Group Study',
            'date' : datetime.date(2022,5,31),
            'time':'9PM',
            'location' : 'Zoom',
            'agenda' : 'lets study together'
            }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

#test is failing
    def test_meetingform_Invalid(self):
        data={
            'title':'Group Study',
            'date' : datetime.date(2022,5,32),
            'location' : 'Zoom',
            'agenda' : 'lets study together'
            }
        form=MeetingForm(data)
        self.assertFalse(form.is_valid)

class NewResourceForm(TestCase):
    def test_resourceform(self):
        data={
            'name':'Learn Python',
            'type' : 'Website',
            'URL':'https://www.learnpython.org/',
            'date entered' : datetime.date(2022,5,31),
            'user' : 'Erin',
            'description' : 'very helpful'
            }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

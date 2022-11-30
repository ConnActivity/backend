# You need to have the server running to test this.
# We need a firebase key.

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from start.models import User, Tag, Event
from start.views import event_list, user_list

factory = APIRequestFactory()
factory.cookies['user_token']: 'Na_i_mog_afach_nimma_oida'  # TODO: This doesn't work somehow


class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(user_id='1', user_bio="Ich bin Bene", username="Bene",
                            user_email="bene@dumm.de", gender='m',
                            university="DHBW")
        User.objects.create(user_id='2', user_bio="Ich bin Maxi, kennen sie schon meine Mikrowelle?", username="maxi",
                            user_email="maxi@cool.de", gender='m',
                            university="APIRequestFactory")
        User.objects.create(user_id='3', user_bio="Ich mog nimma", username="EnteWente",
                            user_email="mary@supitoll.de", gender='w',
                            university="Hochschule der Leute")
        User.objects.create(user_id='4', user_bio="I bims da Flipper", username="Phil",
                            user_email="Phil@fat.ass", gender='m',
                            university="DHBW4")

    # Tests müssen mit test_ beginnen!
    def test_list_users(self):
        request = factory.get('/user/')
        request.COOKIES['user_token'] = 'Na_i_mog_afach_nimma_oida'
        # Call the view method directly and pass in our fake request
        response = user_list(request).render()
        # Now we can look at the response and see if it's what we expect
        self.assertEqual(response.status_code, 418)

    def test_create_user(self):
        # Hier könnten ihre Daten stehen(z.B. event-name etc wie bei Postman)
        data = {
            "user_id": "5",
            "user_bio": "Ich bin Maxi King",
            "username": "Maxi_King",
            "user_email": "Maxi@king.de",
            "gender": "x",
            "university": "404",
            "user_tags": [1]
        }
        Tag.objects.create(value="Bayern")
        request = factory.post('/user/', data)
        request.COOKIES['user_token'] = 'Na_i_mog_afach_nimma_oida'
        response = user_list(request).render()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data,
                         {'user_id': '73', 'username': 'Maxi_King', 'gender': 'x', 'user_email': 'Maxi@king.de',
                          'user_age': 0, 'university': '404', 'user_bio': 'Ich bin Maxi King', 'user_tags': [1]})
        # self.assertEqual(response.data, data)


class EventTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(value="Koksen")
        Tag.objects.create(value="Banküberfall")
        Tag.objects.create(value="Saufen")
        User.objects.create(user_id='1', user_bio="Ich bin Bene", username="Bene",
                            user_email="bene@dumm.de", gender='m',
                            university="DHBW")
        Event.objects.create(id=1, title="Koksen-Event", date_published="2019-01-01", date="2019-01-01",
                             location="Koksen", description="Koksen-Event", member_limit=10,
                             is_private=False, creator=User.objects.get(user_id=1))
        event = Event.objects.get(id=1)
        event.tags.add(Tag.objects.get(value="Koksen"))
        event.tags.add(Tag.objects.get(value="Banküberfall"))
        event.member_list.add(User.objects.get(user_id=1))
        event.member_wait_list.add(User.objects.get(user_id=1))
        event.save()

    def test_create_event(self):
        data = {
            "title": "Saufen-Event",
            "date_published": "2019-01-01",
            "date": "2019-01-01",
            "location": "Saufen",
            "description": "Saufen-Event",
            "member_limit": 10,
            "tags": [1, 2],
            "member_list": [73],
            "is_private": False,
            "member_wait_list": [],
            "creator": 73
        }
        request = factory.post('/event/', data)
        request.COOKIES['user_token'] = 'Na_i_mog_afach_nimma_oida'
        response = event_list(request).render()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, data)

    def test_leave_event(self):
        usertests = UserTests()
        UserTests.test_create_user(usertests)
        self.test_create_event()
        data = {
            "id": 1
        }
        request = factory.put('/leave_event/', data)
        request.COOKIES['user_token'] = 'Na_i_mog_afach_nimma_oida'
        response = event_list(request).render()
        self.assertEqual(response.status_code, 403)
        # TODO: Test with another user that is not the creator

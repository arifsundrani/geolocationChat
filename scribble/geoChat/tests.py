from django.test import TestCase, Client, RequestFactory
from geoChat.views import *
from django.contrib.auth.views import login

# Models
class RegionCoordinatesTest(TestCase):
    def test_region_was_made(self):
        z = RegionCoordinates.objects.create(x1=1, x2=2, y1=1, y2=2)
        z.save()
        self.assertEqual(z.x1, 1)
        self.assertEqual(z.x2, 2)
        self.assertEqual(z.y1, 1)
        self.assertEqual(z.y2, 2)


class ChatRoomTest(TestCase):
    def test_room_was_made(self):
        a = ChatRoom.objects.create(name='Emory',long=2,lat=2)
        a.save()
        self.assertEqual(a.name, 'Emory')
        self.assertEqual(a.active, True)
        self.assertEqual(a.long,2)
        self.assertEqual(a.lat,2)


class PageModelTest(TestCase):
    def test_page_was_made(self):
        b = Page.objects.create(createDate=timezone.now(), topic='Testing',
                                location=RegionCoordinates.objects.create(x1=1, x2=2, y1=1, y2=2))
        b.save()
        self.assertEqual(b.topic, 'Testing')


class CommentTest(TestCase):
    def test_comment_was_made(self):
        c = Comment.objects.create(text='This chat room is wicked cool.', postDate=timezone.now(),
                                   user_name='AnonymousUser')
        c.save()
        self.assertEqual(c.user_name, 'AnonymousUser')
        self.assertEqual(c.active, True)
        self.assertEqual(c.text, 'This chat room is wicked cool.')
        self.assertEqual(c.spam,False)


#Views
class RegisterTest(TestCase):
    def test_register(self):
        v = Client()
        response = v.post('/register/', {'username': 'arif', 'password1': 'nope', 'password2': 'nope'})
        self.assertEqual(response.status_code,302)

#
class LoginTest(TestCase):
    def test_login(self):
        u = Client()
        response = u.post('/login/', {'username': 'test', 'password': 'nope'})
        self.assertEqual(response.status_code,200)

class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', password='test')
        self.chatRoom = ChatRoom.objects.create(name='testing',long=2,lat=2)

    def test_login(self):
        request = self.factory.get('/login/')
        request.user = self.user
        response = login(request)
        self.assertEqual(response.status_code, 200)

    def test_create_room(self):
        request = self.factory.get('/createRoom/')
        request.user = self.user
        response = createRoom(request)
        #print response.status_code
        self.assertEqual(response.status_code, 302)

    def test_create_new_chat(self):
        request = self.factory.get('/')
        request.user = self.user
        response = createNewChat(request)
        self.assertEqual(response.status_code, 200)

    def test_show_settings(self):
        request = self.factory.get('/settings/')
        request.user = self.user
        response = showSettings(request)
        self.assertEqual(response.status_code, 200)

    def test_chat_room(self):
        request = self.factory.get('/chats/1/')
        request.user = self.user
        response = chat_room(request, 1)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        request = self.factory.get('/chats/1/')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        c = Client()
        response = c.post('/logout/', {'username': 'test', 'password': 'nope'})
        self.assertEqual(response.status_code,302)
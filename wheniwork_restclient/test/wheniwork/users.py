from django.test import TestCase
from wheniwork_restclient.wheniwork.users import Users
from wheniwork_restclient.models.wheniwork import User


class WhenIWorkTestUsers(TestCase):
    def test_get_user(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.wheniwork.File'):
            wheniwork = Users()

            user = wheniwork.get_user(188885)

            self.assertEquals(user.id, 188885, "Has correct user id")
            self.assertEquals(user.first_name, "Joe", "Has correct first name")
            self.assertEquals(user.last_name, "User", "Has correct last name")
            self.assertEquals(user.email, "testid99@foo.com", "Has correct email")

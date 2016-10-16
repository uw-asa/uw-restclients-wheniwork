from django.test import TestCase
from wheniwork_restclient.wheniwork.users import Users


class WhenIWorkTestUsers(TestCase):

    def test_users(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = Users()

            user = wheniwork.get_user(4364)
            self.assertEquals(user.id, 4364, "Has correct user id")
            self.assertEquals(user.first_name, "Goldie",
                              "Has correct first name")
            self.assertEquals(user.last_name, "Wilson",
                              "Has correct last name")
            self.assertEquals(user.email,
                              "goldiewilson@hillvalleycalifornia.gov",
                              "Has correct email")

            users = wheniwork.get_users()
            self.assertEquals(users[1].first_name, "Jennifer")
            self.assertEquals(users[1].last_name, "Parker")
            self.assertEquals(users[1].email, "jen.parker@example.com")

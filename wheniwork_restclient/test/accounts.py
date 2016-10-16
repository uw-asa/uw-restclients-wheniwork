from django.test import TestCase
from wheniwork_restclient.wheniwork.account import Accounts as WhenIWork


class WhenIWorkTestAccounts(TestCase):

    def test_accounts(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = WhenIWork()

            account = wheniwork.get_account()
            self.assertEquals(account.id, 11)
            self.assertEquals(account.company, '123 Company')

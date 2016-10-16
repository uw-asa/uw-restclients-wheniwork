from django.test import TestCase
from django.conf import settings
from wheniwork_restclient.wheniwork.account import Accounts as WhenIWork
from wheniwork_restclient.exceptions import DataFailureException


class WhenIWorkTestAccounts(TestCase):

    def test_account(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'wheniwork.File'):
            wheniwork = WhenIWork()

            account = wheniwork.get_account(341132)
            self.assertEquals(account.id, 341132)
            self.assertEquals(account.company, "UW-IT CTE", "Has proper name")
            self.assertEquals(account.master_id, 0)

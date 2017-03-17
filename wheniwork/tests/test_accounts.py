from unittest import TestCase

from wheniwork.account import Accounts
from wheniwork.util import fdao_wheniwork_override


@fdao_wheniwork_override
class WhenIWorkTestAccounts(TestCase):

    def test_accounts(self):
        wheniwork = Accounts()

        account = wheniwork.get_account()
        self.assertEquals(account.account_id, 11)
        self.assertEquals(account.company, '123 Company')

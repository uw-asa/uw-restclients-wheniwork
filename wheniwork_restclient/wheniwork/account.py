from wheniwork_restclient.wheniwork import WhenIWork
from wheniwork_restclient.models import Account


class Accounts(WhenIWork):
    def get_account(self):
        """
        Get Existing Account

        http://dev.wheniwork.com/#get-existing-account
        """
        url = "/2/account/"
        return self._account_from_json(self._get_resource(url)["account"])

    def _account_from_json(self, data):
        account = Account()
        account.account_id = data["id"]
        account.company = data["company"]
        account.master_id = data["master_id"]
        return account

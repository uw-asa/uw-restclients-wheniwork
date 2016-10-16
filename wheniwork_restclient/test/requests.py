from django.test import TestCase
from wheniwork_restclient.wheniwork.requests import Requests as WhenIWork


class WhenIWorkTestRequests(TestCase):

    def test_requests(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = WhenIWork()

            requests = wheniwork.get_requests({'start': '2012-03-01',
                                               'end': '2012-04-30'})
            self.assertEquals(requests[0].user_id, 135)
            self.assertEquals(requests[1].user_id, 135)

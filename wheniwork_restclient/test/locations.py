from django.test import TestCase
from wheniwork_restclient.wheniwork.locations import Locations as WhenIWork


class WhenIWorkTestLocations(TestCase):

    def test_locations(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = WhenIWork()

            locations = wheniwork.get_locations()
            self.assertEquals(locations[0].location_id, 136)
            self.assertEquals(locations[1].address, '100 Courthouse Square, '
                                                    'Hill Valley, CA 12345')

            location = wheniwork.get_location(136)
            self.assertEquals(location.name, 'Downtown')

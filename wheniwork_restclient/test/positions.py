from django.test import TestCase
from wheniwork_restclient.wheniwork.positions import Positions as WhenIWork


class WhenIWorkTestPositions(TestCase):

    def test_positions(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = WhenIWork()

            positions = wheniwork.get_positions()
            self.assertEquals(positions[0].name, 'Stocker')
            self.assertEquals(positions[1].name, 'Bagger')
            self.assertEquals(positions[2].name, 'Cashier')

            position = wheniwork.get_position(32)
            self.assertEquals(position.name, 'Stocker')

from django.test import TestCase
from wheniwork_restclient.wheniwork.shifts import Shifts


class WhenIWorkTestShifts(TestCase):

    def test_shifts(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = Shifts()

            shifts = wheniwork.get_shifts({
                'location_id': 1,
                'start': '2014-03-05 00:00:00',
                'end': '2014-03-08 23:59:59',
            })
            self.assertEquals(shifts[0].id, 10000)
            self.assertEquals(shifts[1].site_id, 4351)
            self.assertEquals(shifts[1].notes, 'We need more cowbell.')

            shift = wheniwork.create_shift({
                'notes': 'Come in early today.'
            })
            self.assertEquals(shift.notes, 'Come in early today.')

            ret = wheniwork.delete_shifts([1337])
            self.assertTrue(ret["success"])

from django.test import TestCase
from wheniwork_restclient.wheniwork.sites import Sites as WhenIWork


class WhenIWorkTestSites(TestCase):

    def test_sites(self):
        with self.settings(
                WHENIWORK_DAO_CLASS='wheniwork_restclient.dao_implementation.'
                                    'File'):
            wheniwork = WhenIWork()

            sites = wheniwork.get_sites()
            self.assertEquals(sites[0].name, 'Twin Pines')
            self.assertEquals(sites[1].name, 'Lone Pine')

            site = wheniwork.get_site(9)
            self.assertEquals(site.address, '1600 S Azusa Ave, '
                                            'City of Industry, CA 91748')

            site = wheniwork.create_site({
                'name': 'Shaded Grove',
            })
            self.assertEquals(site.name, 'Shaded Grove')

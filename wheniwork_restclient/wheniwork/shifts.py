from wheniwork_restclient.wheniwork import WhenIWork
from wheniwork_restclient.models import Shift
from wheniwork_restclient.wheniwork.locations import Locations
from wheniwork_restclient.wheniwork.sites import Sites
from wheniwork_restclient.wheniwork.positions import Positions
from wheniwork_restclient.wheniwork.users import Users
import dateutil.parser
from urllib import urlencode


class Shifts(WhenIWork):
    def get_shifts(self, params={}):
        """
        List shifts

        http://dev.wheniwork.com/#listing-shifts
        """
        url = "/2/shifts/?%s" % urlencode(params)

        data = self._get_resource(url)
        shifts = []
        locations = {}
        sites = {}
        positions = {}
        users = {}
        for entry in data.get("locations", []):
            location = Locations()._location_from_json(entry)
            locations[location.location_id] = location
        for entry in data.get("sites", []):
            site = Sites()._site_from_json(entry)
            sites[site.site_id] = site
        for entry in data.get("positions", []):
            position = Positions()._position_from_json(entry)
            positions[position.position_id] = position
        for entry in data.get("users", []):
            user = Users()._user_from_json(entry)
            users[user.user_id] = user
        for entry in data["shifts"]:
            shift = self._shift_from_json(entry)
            shifts.append(shift)

        for shift in shifts:
            shift.location = locations.get(shift.location_id, None)
            shift.site = sites.get(shift.site_id, None)
            shift.position = positions.get(shift.position_id, None)
            shift.user = users.get(shift.user_id, None)

        return shifts

    def create_shift(self, params={}):
        """
        Creates a shift

        http://dev.wheniwork.com/#create/update-shift
        """
        url = "/2/shifts/"
        body = params

        data = self._post_resource(url, body)
        shift = self._shift_from_json(data["shift"])
        shift.save()

        return shift

    def delete_shifts(self, shifts):
        """
        Delete existing shifts.

        http://dev.wheniwork.com/#delete-shift
        """
        url = "/2/shifts/?%s" % urlencode(
            {'ids': ",".join(str(s) for s in shifts)})

        data = self._delete_resource(url)

        return data

    def _shift_from_json(self, data):
        shift = Shift()
        shift.shift_id = data['id']
        shift.user_id = data['user_id']
        shift.account_id = data['account_id']
        shift.location_id = data['location_id']
        if data['position_id']:
            shift.position_id = data['position_id']
        if data['site_id']:
            shift.site_id = data['site_id']
        if 'start_time' in data and data['start_time']:
            shift.start_time = dateutil.parser.parse(data['start_time'])
        if 'end_time' in data and data['end_time']:
            shift.end_time = dateutil.parser.parse(data['end_time'])
        shift.notes = data['notes']
        return shift

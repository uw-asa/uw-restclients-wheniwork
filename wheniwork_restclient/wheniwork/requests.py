from wheniwork_restclient.wheniwork import WhenIWork
from wheniwork_restclient.models import Request
from wheniwork_restclient.wheniwork.users import Users
from wheniwork_restclient.wheniwork.messages import Messages
import dateutil.parser
from urllib import urlencode


class Requests(WhenIWork):
    def get_requests(self, params={}):
        """
        List requests

        http://dev.wheniwork.com/#listing-requests
        """
        if "status" in params:
            params['status'] = ','.join(map(str, params['status']))

        requests = []
        users = {}
        messages = {}
        params['page'] = 0
        while True:
            url = "/2/requests/?%s" % urlencode(params)

            data = self._get_resource(url)
            for entry in data["users"]:
                user = Users()._user_from_json(entry)
                users[user.user_id] = user
            for entry in data["requests"]:
                request = self._request_from_json(entry)
                requests.append(request)
            for entry in data["messages"]:
                message = Messages()._message_from_json(entry)
                if message.request_id not in messages:
                    messages[message.request_id] = []
                messages[message.request_id].append(message)

            if not data['more']:
                break

            params['page'] += 1

        for request in requests:
            request.user = users.get(request.user_id, None)
            request.messages = messages.get(request.request_id, [])

        return requests

    def _request_from_json(self, data):
        request = Request()
        request.request_id = data['id']
        request.account_id = data['account_id']
        request.user_id = data['user_id']
        request.creator_id = data['creator_id']
        request.status = data['status']
        request.type = data['type']
        request.start_time = dateutil.parser.parse(data['start_time'])
        request.end_time = dateutil.parser.parse(data['end_time'])
        request.created_at = dateutil.parser.parse(data['created_at'])
        request.updated_at = dateutil.parser.parse(data['updated_at'])
        request.canceled_by_id = data['canceled_by'] \
            if 'canceled_by' in data else 0

        request.hours = str(data['hours'])
        return request

"""
Contains When I Work DAO implementations.
"""

from wheniwork_restclient.dao_implementation.live import get_live_url
from wheniwork_restclient.dao_implementation.mock import get_mockdata_url, \
    post_mockdata_url, delete_mockdata_url, put_mockdata_url, \
    convert_to_platform_safe
from django.conf import settings
from os.path import abspath, dirname


class File(object):
    """
    The File DAO implementation returns generally static content.  Use this
    DAO with this configuration:

    WHENIWORK_DAO_CLASS =
    'wheniwork_restclient.dao_implementation.wheniwork.File'
    """
    def getURL(self, url, headers):
        return get_mockdata_url("wheniwork", "file", url, headers)

    def putURL(self, url, headers, body):
        response = put_mockdata_url("wheniwork", "file", url, headers, body)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/wheniwork/file" +
                       url + ".PUT")

        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response

    def postURL(self, url, headers, body):
        response = post_mockdata_url("wheniwork", "file", url, headers, body)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/wheniwork/file" +
                       url + ".POST")
        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response

    def deleteURL(self, url, headers):
        response = delete_mockdata_url("wheniwork", "file", url, headers)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/wheniwork/file" +
                       convert_to_platform_safe(url) + ".DELETE")
        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response


class Live(object):
    """
    This DAO provides real data.  It requires the following configuration:

    WHENIWORK_HOST="api.wheniwork.com"
    WHENIWORK_TOKEN="..."
    """
    ignore_security = getattr(settings,
                              'WHENIWORK_IGNORE_CA_SECURITY',
                              False)

    verify_https = True
    if ignore_security:
        verify_https = False

    def getURL(self, url, headers):
        host = settings.WHENIWORK_HOST
        token = settings.WHENIWORK_TOKEN

        if "W-Token" not in headers:
            headers["W-Token"] = "%s" % token

        return get_live_url('GET',
                            host, url, headers=headers)

    def putURL(self, url, headers, body):
        host = settings.WHENIWORK_HOST
        token = settings.WHENIWORK_TOKEN

        if "W-Token" not in headers:
            headers["W-Token"] = "%s" % token

        return get_live_url('PUT',
                            host, url, headers=headers, body=body)

    def postURL(self, url, headers, body):
        host = settings.WHENIWORK_HOST
        token = settings.WHENIWORK_TOKEN

        if "W-Token" not in headers:
            headers["W-Token"] = "%s" % token

        return get_live_url('POST',
                            host, url, headers=headers, body=body)

    def deleteURL(self, url, headers):
        host = settings.WHENIWORK_HOST
        token = settings.WHENIWORK_TOKEN

        if "W-Token" not in headers:
            headers["W-Token"] = "%s" % token

        return get_live_url('DELETE',
                            host, url, headers=headers)

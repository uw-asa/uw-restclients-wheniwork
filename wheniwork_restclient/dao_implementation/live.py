"""
Provides access to the http connection pools and
connections for live data from a web service

"""

import ssl
from urlparse import urlparse
import certifi
import urllib3


def get_live_url(method,
                 host,
                 url,
                 headers,
                 body=None):
    """
    Return a connection from the pool and perform an HTTP request.
    :param method:
        HTTP request method (such as GET, POST, PUT, etc.)
    :param host:
        the server host.
    :param host:
        the url.
    :param headers:
        headers to include with the request
    :param body:
        the POST, PUT body of the request
    """
    kwargs = {}

    if urlparse(host).scheme == "https":
        kwargs["ssl_version"] = ssl.PROTOCOL_TLSv1
        kwargs["cert_reqs"] = "CERT_REQUIRED"
        kwargs["ca_certs"] = certifi.where()

    con_pool = urllib3.PoolManager(kwargs)

    url = host + url

    response = con_pool.urlopen(method, url, body=body, headers=headers)
    return response

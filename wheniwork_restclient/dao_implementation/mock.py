import sys
import os
from os.path import abspath, dirname
import re
import json
import logging
import time
import socket
from urllib import quote, unquote, urlencode
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from importlib import import_module
from wheniwork_restclient.mock_http import MockHTTP


"""
A centralized the mock data access
"""
# Based on django.template.loaders.app_directories
fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
app_resource_dirs = []

# An issue w/ loading order in management commands means this needs to be
# a function.  Otherwise we can be trying to load modules that are trying to
# load this code, and python bails on us.


def __initialize_app_resource_dirs():
    if len(app_resource_dirs) > 0:
        return
    for app in settings.INSTALLED_APPS:
        try:
            mod = import_module(app)
        except ImportError, e:
            raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))

        resource_dir = os.path.join(os.path.dirname(mod.__file__), 'resources')
        if os.path.isdir(resource_dir):
            # Cheating, to make sure our resources are overridable
            data = {
                'path': resource_dir.decode(fs_encoding),
                'app': app,
            }
            if app == 'restclients':
                app_resource_dirs.append(data)
            else:
                app_resource_dirs.insert(0, data)


def get_mockdata_url(service_name, implementation_name,
                     url, headers):
    """
    :param service_name:
        possible "wheniwork"
    :param implementation_name:
        possible values: "file", etc.
    """

    dir_base = dirname(__file__)
    __initialize_app_resource_dirs()

    RESOURCE_ROOT = abspath(dir_base + "/../resources/" +
                            service_name + "/" + implementation_name)

    file_path = None
    success = False
    start_time = time.time()

    for resource_dir in app_resource_dirs:
        response = _load_resource_from_path(resource_dir, service_name,
                                            implementation_name, url, headers)

        if response:
            return response

    # If no response has been found in any installed app, return a 404
    logger = logging.getLogger(__name__)
    logger.info("404 for url %s, path: %s" %
                (url, "resources/%s/%s/%s" %
                 (service_name,
                  implementation_name,
                  convert_to_platform_safe(url))))
    response = MockHTTP()
    response.status = 404
    return response


def _load_resource_from_path(resource_dir, service_name,
                             implementation_name,
                             url, headers):

    RESOURCE_ROOT = os.path.join(resource_dir['path'],
                                 service_name,
                                 implementation_name)
    app = resource_dir['app']

    if url == "///":
        # Just a placeholder to put everything else in an else.
        # If there are things that need dynamic work, they'd go here
        pass
    else:
        orig_file_path = RESOURCE_ROOT + url
        unquoted = unquote(orig_file_path)
        paths = [
            convert_to_platform_safe(orig_file_path),
            "%s/index.html" % (convert_to_platform_safe(orig_file_path)),
            orig_file_path,
            "%s/index.html" % orig_file_path,
            convert_to_platform_safe(unquoted),
            "%s/index.html" % (convert_to_platform_safe(unquoted)),
            unquoted,
            "%s/index.html" % unquoted,
            ]

        file_path = None
        handle = None
        for path in paths:
            try:
                file_path = path
                handle = open(path)
                break
            except IOError as ex:
                pass

        if handle is None:
            return None

        logger = logging.getLogger(__name__)
        logger.debug("URL: %s; App: %s; File: %s" % (url, app, file_path))

        response = MockHTTP()
        response.status = 200
        response.data = handle.read()
        response.headers = {"X-Data-Source": service_name + " file mock data",
                            }

        try:
            headers = open(handle.name + '.http-headers')
            file_values = json.loads(headers.read())

            if "headers" in file_values:
                response.headers = dict(response.headers.items() +
                                        file_values['headers'].items())

                if 'status' in file_values:
                    response.status = file_values['status']

            else:
                response.headers = dict(response.headers.items() +
                                        file_values.items())

        except IOError:
            pass

        return response


def post_mockdata_url(service_name, implementation_name,
                      url, headers, body,
                      dir_base=dirname(__file__)):
    """
    :param service_name:
        possible "sws", "pws", "book", "hfs", etc.
    :param implementation_name:
        possible values: "file", etc.
    """
    # Currently this post method does not return a response body
    response = MockHTTP()
    if body is not None:
        if "dispatch" in url:
            response.status = 200
        else:
            response.status = 201
        response.headers = {"X-Data-Source": service_name + " file mock data",
                            "Content-Type": headers['Content-Type']}
    else:
        response.status = 400
        response.data = "Bad Request: no POST body"
    return response


def put_mockdata_url(service_name, implementation_name,
                     url, headers, body,
                     dir_base=dirname(__file__)):
    """
    :param service_name:
        possible "sws", "pws", "book", "hfs", etc.
    :param implementation_name:
        possible values: "file", etc.
    """
    # Currently this put method does not return a response body
    response = MockHTTP()
    if body is not None:
        response.status = 204
        response.headers = {"X-Data-Source": service_name + " file mock data",
                            "Content-Type": headers['Content-Type']}
    else:
        response.status = 400
        response.data = "Bad Request: no POST body"
    return response


def delete_mockdata_url(service_name, implementation_name,
                        url, headers,
                        dir_base=dirname(__file__)):
    """
    :param service_name:
        possible "sws", "pws", "book", "hfs", etc.
    :param implementation_name:
        possible values: "file", etc.
    """
    # Http response code 204 No Content:
    # The server has fulfilled the request but does not need to
    # return an entity-body
    response = MockHTTP()
    response.status = 204

    return response


def convert_to_platform_safe(dir_file_name):
    """
    :param dir_file_name: a string to be processed
    :return: a string with all the reserved characters replaced
    """
    return re.sub('[\?|<>=:*,;+&"@]', '_', dir_file_name)

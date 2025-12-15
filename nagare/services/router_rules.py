# --
# Copyright (c) 2014-2025 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from webob import exc
from peak.rules import when

from nagare.services import plugin


class Router(plugin.Plugin):
    """A service wrapped around the router.

    Being now a service, the router can be injected
    """

    def create_dispatch_args(self, request, response, **params):
        path_info = request.path_info.strip('/')
        url = path_info.split('/') if path_info else ()

        return tuple(url), request.method, request, response

    def __call__(self, o, url, http_method, request, response):
        return route(o, url, http_method, request, response)


def route(o, url, http_method, request, response):
    """Fallback when no route is found.

    In:
      - ``o`` -- the object
      - ``url`` -- the URL
      - ``http_method`` -- the HTTP method
      - ``request`` -- the WebOb request object
      - ``response`` -- the WebOb response object
    """
    raise exc.HTTPNotFound()


def route_for(cls, cond=None, methods=('GET', 'HEAD')):
    """Decorator helper to register an URL for a class of objects.

    In:
      - ``cls`` -- the class
      - ``cond`` -- a generic condition

    Return:
      - a closure
    """
    conds = []

    if not cond and not methods:
        # No condition given, dispatch on the class
        conds.append((cls,))

    if cond:
        conds.append(f'isinstance(o, {cls.__name__}) and ({cond})')

    if methods:
        conds.append('(http_method in %r)' % (methods,))

    return when(route, ' and '.join(conds))

from __future__ import absolute_import, print_function

from .provider import *  # NOQA
from .manager import ProviderManager
from .view import *  # NOQA

providers = ProviderManager()
register = default_manager.register
unregister = default_manager.unregister

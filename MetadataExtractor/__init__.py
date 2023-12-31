import logging
from logging import NullHandler

from ._version import __version__

# This is a namespace package, don't put any functional code in here besides the
# declare_namespace call, or it will disappear on install. See:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#namespace-packages
__import__("pkg_resources").declare_namespace(__name__)

logging.getLogger(__name__).addHandler(NullHandler())

# ... Clean up.
del NullHandler

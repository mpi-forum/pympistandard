"""
This module defines the handy export decorator which adds the function to the __all__.

https://stackoverflow.com/a/35710527
"""


from typing import Callable
import sys


def export(func) -> Callable:
    """Adds fn to __all__ in the a module."""

    mod = sys.modules[func.__module__]

    if hasattr(mod, '__all__'):
        mod.__all__.append(func.__name__)
    else:
        mod.__all__ = [func.__name__]

    return func

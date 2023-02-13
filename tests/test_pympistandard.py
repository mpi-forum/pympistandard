"""
This module tests basic functionality of the pympistandard module.
"""


import pytest


def test_load():
    try:
        import pympistandard as std

        std.use_api_version(1)

    except AttributeError:
        pytest.fail(
            "AttributeError: module 'importlib.resources' has no attribute 'files'"
        )

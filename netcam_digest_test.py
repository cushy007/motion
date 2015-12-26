# coding: utf-8

import pytest
import sys

import motion_api


@pytest.fixture
def headers():
	return """polop"""


def test_http_digest_01a(headers):
	"""  """
	print(headers)
	assert motion_api.http_digest("qwerty") == 7

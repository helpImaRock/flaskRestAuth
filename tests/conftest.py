import os
import pytest

from myApp import create_app

@pytest.fixture(scope='module')
def test_client():

	flask_app = create_app(None)

	with flask_app.test_client() as test_client:
		with flask_app.app_context():
			pass
		yield test_client
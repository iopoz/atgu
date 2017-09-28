from time import sleep

import pytest


@pytest.yield_fixture(scope='session', autouse=True)
def init(app, env):
    print('SetUP')
    app.general.open_portal(env.Server.url)
    yield


class TestTest:
    def test_1(self, app):
        app.general.close_location_choosing()
        assert app.general.is_portal_ready()
        app.general.go_to_catalog_screen()
        app.general.go_to_home_screen()
        assert app.general.is_home_screen()
        sleep(3)
import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file)
        with open(config_file) as opened_file:
            target = json.load(opened_file)
    return target

@pytest.fixture(scope='session')
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture
def app(request,config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser= browser, config = config)
    return fixture


@pytest.fixture()
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption ("--browser", action='store', default='chrome')
    parser.addoption("--target", action='store', default='target.json')





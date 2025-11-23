import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        driver = item.funcargs.get("setup")
        driver.save_screenshot("failed.png")










class TestDemo:
    def test_google_title(self, setup):
        assert "GoogleAA" in self.driver.title

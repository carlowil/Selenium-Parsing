from scrap_func import *


class Browser:
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self, times):
        height = 800
        for i in range(times):
            self.driver.execute_script("window.scrollTo(0, %s)" % str(height))
            height += 800
            time.sleep(PAUSE_TIME)

    def get_url(self, url):
        self.driver.get(url)

    def close_driver(self):
        self.driver.close()

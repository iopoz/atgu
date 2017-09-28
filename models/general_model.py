from pages.general_page import GeneralPage


class GeneralModel(object):
    def __init__(self, app):
        self.app = app
        self.gp = GeneralPage()

    def open_portal(self, url):
        return self.gp.driver.get(url)

    def close_location_choosing(self):
        return self.gp.place_locator_btn_close.click()

    def go_to_catalog_screen(self):
        return self.gp.catalog_btn.click()

    def go_to_home_screen(self):
        return self.gp.general_btn.click()

    def is_home_screen(self):
        return self.gp.popular_panel.is_displayed()

    def is_portal_ready(self):
        return self.gp.page_frame.is_displayed()
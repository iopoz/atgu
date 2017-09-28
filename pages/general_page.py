from pages.page import Page


class GeneralPage(Page):
    @property
    def place_locator_btn_close(self):
        return self.wait_element_by_path(".//div[contains(@class,'close_popup_x')]")

    @property
    def catalog_btn(self):
        return self.wait_clickable_element_by_path(".//li[contains(@class, 'catalog-on-main-trigger')]")

    @property
    def general_btn(self):
        return self.wait_element_by_path(".//li[@class='home']")

    @property
    def popular_panel(self):
        return self.wait_element_by_path(".//div[@class='index-popular']")

    @property
    def page_frame(self):
        return self.wait_clickable_element_by_path("//*[@id='data-ng-app']/body/iframe")
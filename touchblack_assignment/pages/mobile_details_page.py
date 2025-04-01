import yaml
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class mobileDetailPage(BasePage):
    mobile_link = (By.LINK_TEXT, "Samsung galaxy s6")
    mobile_price = (By.XPATH, "//h5[normalize-space()='$360']")

    mobile_image_view_page = (By.XPATH, "//div[@class='item active']//img")

    mobile_name_view_page = (By.XPATH, "//h2[normalize-space()='Samsung galaxy s6']")

    mobile_price_view_page = (By.XPATH, "//h3[@class='price-container'][1]")

    mobile_name = (By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")


    def navigate_to_mobile_view_page(self):
        mobile_product = self.find_element(self.mobile_name).text
        price = self.find_element(self.mobile_price).text
        self.click_element(self.mobile_link)
        self.wait_for_element_visible(self.mobile_image_view_page)
        return mobile_product, price

    def current_url(self):
        return self.get_current_url()

    def verify_mobile_application(self):
        verify_mobile_name = self.find_element(self.mobile_name_view_page).text
        verify_mobile_price = self.find_element(self.mobile_price_view_page).text
        results = dict()
        results['verify_mobile_name'] = verify_mobile_name
        results['verify_mobile_price'] = verify_mobile_price
        return results


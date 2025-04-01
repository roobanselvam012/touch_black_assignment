from pages.mobile_details_page import mobileDetailPage
from utils.logger import log


def test_verify_mobile_application(driver):
    log.info("Mobile product check exection started")

    mobile_page = mobileDetailPage(driver)

    navigate_to_mobile_product = mobile_page.navigate_to_mobile_view_page()

    mobile_name  = navigate_to_mobile_product[0]
    mobile_price = navigate_to_mobile_product[1]

    log.info(mobile_name)
    log.info(mobile_price)

    mobile_view_page_url = mobile_page.current_url()

    assert "idp_=1" in mobile_view_page_url, "Wrong product url navigated"

    log.info(mobile_view_page_url)

    verify_mobile_product_details = mobile_page.verify_mobile_application()

    log.info(verify_mobile_product_details)

    assert mobile_name == verify_mobile_product_details["verify_mobile_name"], "mobile product assesrtion failed"

    assert mobile_price in verify_mobile_product_details["verify_mobile_price"], "mobile product assesrtion failed"

    log.info("Navigation and mobile product verified")
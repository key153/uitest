import time, logging

import login


def deal_case_error(driver, case_name, e):
    nowTime = time.strftime('test_002' + "%Y%m%d.%H.%M.%S")
    driver.get_screenshot_as_file("error_image\\%s.png" % nowTime)
    logging.info('Fail: ' + case_name)
    logging.error(e)
    login.login_web(driver)
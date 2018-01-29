import time

def get_excetion(driver):
    nowTime = time.strftime('test_001' + "%Y%m%d.%H.%M.%S")
	driver.get_screenshot_as_file("error_image\\%s.png" % nowTime)
    driver.quit()

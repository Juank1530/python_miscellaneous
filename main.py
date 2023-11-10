from selenium.common.exceptions import NoSuchElementException
from pagesSpeedImages import config
from pagesSpeedImages.imagesPagesSpeed import open_browser, get_data_site, open_images

if __name__ == '__main__':

    #list = []
    driver = open_browser(config.CHROME_DRIVER_PATH)
    list_links = get_data_site(driver, config.BASE_URL, config.SITE_URL)

    # while not list:
    #     list = get_data_site(driver, config.BASE_URL, config.SITE_URL)
    #     try:
    #         print('First Attempt')
    #         open_images(driver,list)
    #     except NoSuchElementException:
    #         print("This auditory has been passed")

    if len(list_links) > 0:
        try:
            print('First Attempt')
            open_images(driver,list_links, config.LOG_FILE_PATH)
        except NoSuchElementException:
            print("This auditory has been passed")
    else:
        try:
            print('Second Attempt')
            list_links = get_data_site(driver, config.BASE_URL, config.SITE_URL)
            open_images(driver, list_links, config.LOG_FILE_PATH)
        except NoSuchElementException:
            print("This auditory has been passed")

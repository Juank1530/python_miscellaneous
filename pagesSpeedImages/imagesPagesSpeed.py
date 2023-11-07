from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(driver):
    try:
        # Browser's driver setup
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver_service = Service(executable_path=driver)
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    except Exception as e:
        print(f'Error in driver setup: {e}')
        print(
            'Also you can check the Google driver and update it. Please go to https://chromedriver.chromium.org/downloads  and download the last stable version.')
        sys.exit(1)
    return driver


def get_data_site(driver, url, site_url):
    links = []
    driver.get(url)
    wait = WebDriverWait(driver, 120)
    text_box = wait.until(EC.element_to_be_clickable((By.NAME, "url")))
    text_box.send_keys(site_url)
    time.sleep(2)
    text_box.send_keys(Keys.ENTER)
    desktop = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/span/button[2]")))
    desktop.click()
    try:
        images = wait.until(EC.element_to_be_clickable((By.XPATH,f'(//*[@id="modern-image-formats"]/details/summary/div/div/div[1]/div/span) [2]')))
        images.click()
        table = driver.find_element(By.XPATH,f'(//*[@id="modern-image-formats"]/details/table) [2]')
        rows = table.find_elements(By.TAG_NAME, "tr")
        total_rows = len(rows)
        print(total_rows)

        links = []
        for i in range(2,total_rows):
            element = driver.find_element(By.XPATH,f'(//*[@id="modern-image-formats"]/details/table/tbody/tr[{str(i)}]/td[2]/div/a) [1]')
            href = element.get_attribute("href")
            links.append(href)
    except NoSuchElementException:
        print("This auditory has been passed")
    except TimeoutException:
        print("Timed out waiting for the 'modern-image-formats' element to be visible")

    if not links:
        links = []

    time.sleep(5)

    return links

def open_images(driver,link_list):
    for i in range(1,5):
        for link in link_list:
            driver.get(link)
            time.sleep(2)
    driver.close()






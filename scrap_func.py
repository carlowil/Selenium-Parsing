from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from Item import *
import time

PAUSE_TIME = 1


def init_driver():
    opt = Options()
    opt.add_argument("--user-data-dir=C:/Users/matve/AppData/Local/Google/Chrome/User Data/")
    opt.add_argument("--profile-directory=Profile 2")
    driver = webdriver.Chrome(options=opt)
    driver.execute_cdp_cmd("Page.removeScriptToEvaluateOnNewDocument", {"identifier": "1"})
    driver.maximize_window()
    return driver


def wildberries_search(browser, item):
    searchform = browser.driver.find_element(By.ID, "searchBlock")
    searchbar = searchform.find_element(By.TAG_NAME, "input")
    searchbar_button = searchform.find_element(By.TAG_NAME, "button")
    searchbar.click()
    searchbar.clear()
    time.sleep(PAUSE_TIME)
    searchbar.send_keys(item)
    time.sleep(PAUSE_TIME)
    searchbar_button.click()


def wildberries_get_item_list(browser, count):
    item_list = []
    browser.scroll_page(int(count / 10))
    scrap_list = browser.driver \
        .find_element(By.CLASS_NAME, "product-card-list") \
        .find_elements(By.TAG_NAME, "article")
    for i in scrap_list:
        link = i.find_element(By.CLASS_NAME, "product-card__wrapper").find_element(By.TAG_NAME, "a").get_attribute(
            "href")
        image = i.find_element(By.TAG_NAME, "img").get_attribute("src")
        title = i.find_element(By.CLASS_NAME, "product-card__name").text
        comments = i.find_element(By.CLASS_NAME, "product-card__count").text
        price = i.find_element(By.CLASS_NAME, "price__lower-price").text

        new_item = Item(link=link, img=image, comments=comments, price=price, title=title)

        item_list.append(new_item)
    return item_list


def yandex_market_search(browser, item):
    searchform = browser.driver.find_element(By.TAG_NAME, "form").find_element(By.ID, "header-search")
    searchform.click()
    time.sleep(PAUSE_TIME)
    searchform.clear()
    searchform.send_keys(item)
    time.sleep(PAUSE_TIME)
    searchform.send_keys(Keys.ENTER)


def yandex_get_item_list(browser, count):
    item_list = []
    browser.scroll_page(int(count / 5))
    scrap_list = browser.driver \
        .find_element(By.ID, "searchResults") \
        .find_elements(By.TAG_NAME, "article")
    for i in scrap_list:
        link = i.find_element(By.TAG_NAME, "a").get_attribute("href")
        image = i.find_element(By.TAG_NAME, "img").get_attribute("src")
        title = i.find_element(By.TAG_NAME, "img").get_attribute("title")
        price = i.find_element(By.CLASS_NAME, "UZf17").find_elements(By.TAG_NAME, "span")[1].text

        new_item = Item(link=link, img=image, price=price.replace('\u2009', ''), title=title)
        item_list.append(new_item)
    return item_list


def ym_parse(browser, request):
    browser.get_url("https://market.yandex.ru/")
    time.sleep(5)
    yandex_market_search(browser, request)
    time.sleep(10)
    ym_items = yandex_get_item_list(browser, 30)
    return ym_items


def wb_parse(browser, request):
    browser.get_url("https://www.wildberries.ru/")
    wildberries_search(browser, request)
    time.sleep(5)
    wb_items = wildberries_get_item_list(browser, 50)
    return wb_items

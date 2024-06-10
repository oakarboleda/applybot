import os
import time
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from modules.clickersFinders import *
from modules.helpers import buffer, print_lg
from bs4 import BeautifulSoup
from bs4.element import Tag


def main():
    try:
        login = login()
        search = search()
        pagination = login.get_pagination()
        print_lg("Total pages: ", pagination)
        applied_jobs = login.split_applied_jobs()
        print_lg("Applied Jobs: ", applied_jobs)
    except Exception as e:
        print_lg(e)


class LinkedIn:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)

    def login(self):
        self.driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
        try:
            self.driver.find_element(By.ID, "username").send_keys(config.username)
            time.sleep(1)
            self.driver.find_element(By.ID, "password").send_keys(config.password)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(10)
        except Exception as e:
            print_lg("Login Failed!")
            print_lg(e)

    def search(self):
        time.sleep(10)
        search_key = "software engineer"  # Enter your Search key here to find people
        key = search_key.split()
        keyword = ""
        for key1 in key:
            keyword = keyword + str(key1).capitalize() + "%20"
        keyword = keyword.rstrip("%20")
        self.driver.get(f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location=United%20States")
        time.sleep(10)

    def get_pagination(self):
        try:
            pagination = self.driver.find_element(By.CLASS_NAME, "artdeco-pagination__pages")
            return pagination.text
        except Exception as e:
            print_lg("Pagination not found!")
            print_lg(e)


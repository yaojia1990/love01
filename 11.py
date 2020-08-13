#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 9:23
# @Author  : YaoJa
from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    driver = webdriver.Chrome()
    sleep(1)
    driver.maximize_window()
    sleep(1)
    url = "https://mms.pinduoduo.com/aftersales/setup"
    driver.get(url)
    sleep(9)
    driver.quit()

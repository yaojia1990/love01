#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 9:11
# @Author  : YaoJa
from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    driver = webdriver.Chrome()
    sleep(1)
    driver.maximize_window()
    sleep(1)
    #
    url = "https://mms.pinduoduo.com/orders/list"
    driver.get(url)
    sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/main/div/section[2]/div/div[1]/div[1]/div/div[2]').click()
    sleep(2)
    driver.find_element_by_id('usernameId').send_keys('pdd33465192476')
    sleep(2)
    driver.find_element_by_id('passwordId').send_keys('Huawei@123')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/main/div/section[2]/div/div[1]/div[2]/section/div/div[2]/button').click()
    sleep(10)
    driver.quit()

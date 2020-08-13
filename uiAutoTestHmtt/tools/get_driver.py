#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 20:46
# @Author  : YaoJa
"""工具类存储目录"""
from selenium import webdriver


class GetDriver:
    # 声明变量
    __web_driver = None

    # 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断driver是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()

            # 置空操作  重点 执行完quit后driver对象清空了但driver在内存中的地址没有清空，上面的判断为空一直不为空，只有第一次获取能成功
            cls.__web_driver = None

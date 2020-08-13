#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 8:16
# @Author  : YaoJa
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    """以下为你web项目专属方法"""

    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 点击父选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        sleep(1)
        # 点击包办显示文本元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

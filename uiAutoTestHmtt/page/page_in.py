#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 19:42
# @Author  : YaoJa
"""统一入口类"""
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)
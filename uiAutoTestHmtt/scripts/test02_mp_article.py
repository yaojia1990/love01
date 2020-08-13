#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:35
# @Author  : YaoJa
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep

class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取PageMpLogin对象并调用成功登陆依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        sleep(1)
        # 获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 关闭浏览器
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试发布文章方法
    def test_mp_article(self, title="test001", content="今晚不开心"):
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        # 查看断言信息
        print("发布文章结果为：", self.article.page_get_info())

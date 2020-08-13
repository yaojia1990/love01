#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 19:51
# @Author  : YaoJa
from selenium.webdriver.common.by import By
"""以下数据为自媒体、后台管理url"""
# 自媒体url
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理url
url_mis = "http://ttmis.research.itcast.cn/#/"
"""以下数据为自媒体模块配置数据---项目中所有page信息"""

# 用户名

mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
# 昵称
mp_nickname = (By.CSS_SELECTOR, ".user-name")
# 内容管理
mp_content_manage = By.XPATH, "//span[text()='内容管理']/..."
# 发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章title
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_fir"
# 文章内容，定位body 勿定位到P标题
mp_content = By.CSS_SELECTOR, "#tinymce"
# 封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 发表
mp_submit = By.XPATH, "//*[text()='发表']/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

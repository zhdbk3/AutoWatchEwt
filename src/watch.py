import os
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import config


def delay() -> None:
    """随机延迟一会，范围：基础延迟时间 ~ 基础延迟时间 + 2"""
    time.sleep(config.base_delay_s + random.random() * 2)


def watch() -> None:
    browser: webdriver.Chrome = getattr(webdriver, config.browser_name)(
        service=getattr(webdriver, config.browser_name.lower()).service.Service(config.driver_path)
    )
    browser.implicitly_wait(10)
    # 访问课程列表，登录
    browser.get(config.lesson_list_url)
    browser.find_element(By.ID, 'login__password_userName').send_keys(config.username)
    browser.find_element(By.ID, 'login__password_password').send_keys(config.password)
    browser.find_element(By.CLASS_NAME, 'ant-btn-block').submit()

    # 点击即刻开启
    delay()
    browser.find_element(By.CLASS_NAME, 'ant-btn-primary').click()
    # 点击加载更多（不一定有）
    try:
        browser.find_element(By.CLASS_NAME, 'get-more-16fey').click()
        print('已加载更多')
    except ElementNotInteractableException:
        pass
    # 查找所有"去学习"按钮
    delay()
    buttons = browser.find_elements(By.CLASS_NAME, 'operate-btn-2TCuM')
    print('找到了', len(buttons), '节课')

    os.system('pause')


if __name__ == '__main__':
    watch()

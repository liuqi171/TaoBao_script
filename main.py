
import os
from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.by import By

from os import path

driver = webdriver.Chrome()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def login(url):
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    print("登录前")
    if driver.find_element(By.LINK_TEXT, "亲，请登录"):
        driver.find_element(By.LINK_TEXT, "亲，请登录").click()
        print("请在10秒内完成扫码")
        time.sleep(10)
        driver.get(url)
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(buytime):
    print("进入buy函数1")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("进入buy函数2")
        # 对比时间，时间到的话就点击结算
        print("开始时间：", now)
        if now >= buytime:
            try:
                print("进入buy函数3")
                # 点击抢购
                if driver.find_element(By.ID, "J_SelectAll1"):
                    print("速度点击！！！")
                    driver.find_element(By.ID, "J_SelectAll1").click()
                   # time.sleep(0.09)
                    while now >= buytime:
                        try:
                           # print("赶紧买！！！")
                           # driver.find_element(By.CLASS_NAME, 'go-btn').click()
                            driver.find_element(By.LINK_TEXT, '结 算').click()
                            print("结算时间：", now)
                            driver.find_element(By.LINK_TEXT, '提交订单').click()
                            print("提交订单时间：", now)
                        except:
                            time.sleep(0.02)
            except:
                time.sleep(0.08)
        print(now)
        time.sleep(0.05)


if __name__ == "__main__":
    print_hi('PyCharm')
    # times = input("请输入抢购时间：时间格式：2021-12-29 19:45:00.000000")
    times = "2022-12-17 15:59:59.990000"
    # 时间格式："2022-03-19 11:43:00.000000"
    # 测试可以
    # https://detail.tmall.com/item.htm?spm=a230r.1.14.16.6a903f34xN9uol&id=618488552961&ns=1&abbucket=12&skuId=4988554791826
    # url = input("请输入抢购地址")
    url = "https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.0.0.5af911d9PNLEHu"
    login(url)
    buy(times)

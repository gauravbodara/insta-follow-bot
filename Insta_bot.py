# -*- coding: utf-8 -*-
"""
Created on Wed May  9 11:23:55 2018

@author: admin
"""
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

url="https://www.instagram.com/"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()


login='//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
loginElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(login))
loginElem.click()


Username='Enter username'
Password='Enetr password'

emailFieldID='username'
passFieldID='password'
loginButtonpath='//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button'


emailFieldElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_name(emailFieldID))
passFieldElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_name(passFieldID))
loginButtonElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginButtonpath))
emailFieldElem.clear()
emailFieldElem.send_keys(Username)
passFieldElem.clear()
passFieldElem.send_keys(Password)
loginButtonElem.click()


discover='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/a'
discoverElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(discover))
discoverElem.click()

see_all='//*[@id="react-root"]/section/main/div/div/h2/a'
see_allElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(see_all))
see_allElem.click()

def request():
    follow='//*[@id="react-root"]/section/main/div/ul/div/li[1]/div/div[1]/div[2]/span'
    lists=[]
    for i in range(1,20):
        st='li['
        st2=i
        st3=']'
        fin=st+str(st2)+st3
        lists.append(follow.replace('li[1]',fin))
    
    
    
    for i in lists:
        followElem=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(i))
        followElem.click()
k=5
while k:
    request()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    k=k-1












time.sleep(5)

driver.quit()

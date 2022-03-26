#!/usr/bin/env python
# coding: utf-8

# In[18]:

from selenium import webdriver


from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.common.exceptions import NoSuchElementException
import os
import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


class Bot():
    a=0
    links = []

    comments = ['great','nice','awesome'
    ]

    def __new__(self,use,passw,hasht):
        l=self.login(self,use,passw)
        if(l!="done"):
            return l
        self.like_comment_by_hashtag(self,hasht)
        return "done"

    def login(self, username, password):
        self.driver =  webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        try:
            self.driver.get('https://instagram.com/')
            sleep(5)
            username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            username_input.send_keys(username)
            sleep(1)
            password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            password_input.send_keys(password)
            sleep(1)
        
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
            sleep(3)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() # clicking 'not now btn'
        except :
            err=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/p').text
            self.driver. close()
            return err
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click() # clicking 'not now btn'
        return "done"
    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/'+hashtag)
        
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            # like
            sleep(5)
            self.driver.find_element_by_xpath("//span[@class='fr66n']").click()
            sleep(10)

            # comment
            self.driver.find_element_by_class_name('RxpZH').click() 
            sleep(5)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
            sleep(5)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()






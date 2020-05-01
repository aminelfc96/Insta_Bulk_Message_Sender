import getpass
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

os.system('color b')
os.system('@echo off')
os.system('cls')
welcome = """Instagram BOT"""
print(welcome)
          
print ("Facebook is used to login ")
fbuser = input("Enter Your Facebook Username : ")
fbpass = getpass.getpass('Enter Your Facebook Passowrd : ', stream = None)
userlink = input("Enter The person username : ")
url1 = ('https://www.instagram.com/' + userlink)
text = input("Your Message : ")
num = int(input("How many times you want to send : "))
class InstagramText():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(1)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button')
        fb_btn.click()
        sleep(1)
        fb_username = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_username.send_keys(fbuser)
        fb_password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_password.send_keys(fbpass)
        sleep(0.5)
        fb_login = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login.click()
        sleep(6)
        close_pop_up = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        close_pop_up.click()
        sleep(1)
        self.driver.get(url1)
        profile_choice = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button')
        profile_choice.click()
        sleep(3)
        for y in range(num):
          sleep(0.5)

          message = self.driver.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')
          message.send_keys(text)
          message.send_keys(Keys.ENTER)
        if True:
            self.driver.close()
            os.system('cls')
            print("Done !,"+ str(num) +" Messages has been sent!")                
sender = InstagramText()
sender.login()

                     

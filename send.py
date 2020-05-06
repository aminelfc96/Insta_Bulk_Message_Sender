import getpass
from selenium import webdriver
from time import sleep,time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from random import randrange
import os
import texts;from texts import messagesx

def CLEAR():
 if os.name == "nt": 
   os.system('color b')
   os.system('@echo off')
   os.system('cls')
 else:
   os.system('clear')
CLEAR()
def Interface():
    global fbuser,fbpass,userlink,url1,num,userchoice,x,text 
    x = len(messagesx)
    print("")
    print("By moamine_lfc96")
    print("")
    fbuser = input("Enter Your Instagram Username : ")
    while len(fbuser) == 0:
      fbuser = 'moamine_lfc96' #default
    print("")
    fbpass = getpass.getpass('Enter Your Instagram Passowrd : ', stream = None)
    print("")
    userlink = input("Enter The person username : ")
    while len(userlink) == 0:
      userlink = 'nvm_iwtc'
    url1 = ('https://www.instagram.com/' + userlink)
    print("")
    num = input("How many times you want to send : ")
    while len(num) == 0:
      num = '5'
    print("")
    userchoice = input("Enter your message (M) or send from dict (D) / MD For Mixed : ")
    if userchoice.lower() == 'm':
      print("")
      text = input("Your Message : ")
      print("")
      print("Sending {0} to : ".format(text) + userlink,str(num) + " times")
    elif userchoice.lower() == 'd' :
      print("")
      print("Sending From Dictioanry to : " + userlink,str(num) + " times")
    elif userchoice.lower() == 'md':
      print("")
      text = input("Your Message : ")
      print("Sending Mixed Messages to : " + userlink,str(num) + " times")
      
CLEAR()
Interface()
class InstagramText():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver.exe')
    def login(self):
        global start 
        start = time()
        self.driver.get('https://www.instagram.com/')
        sleep(3)
        print("")
        print("Try to login..")
        user_name = self.driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')
        user_name.send_keys(fbuser)
        pass_word = self.driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
        pass_word.send_keys(fbpass)
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        login_btn.click()
        sleep(5)
        try:
         close_pop_up = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
         close_pop_up.click()
        except NoSuchElementException as exception:
         print("Error during closing pop-up")

        sleep(1)
        print("")
        print("Logged In Successfully")
    def Sender(self):
        self.driver.get(url1)
        profile_choice = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button')
        profile_choice.click()
        print("")
        print("Preparing to Send ")
        sleep(3)
        print("")
        for y in range(int(num)):
          sleep(0.5)
          w = str(y + 1)
          z = randrange(x)
          message = self.driver.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')
          if userchoice.lower() == 'd':

            message.send_keys(Keys.ENTER)
            message.send_keys(messagesx[z])
            print("-----------------------------------")          
            print("0"+w+"# Sending " + messagesx[z])
          elif userchoice.lower() == 'm':

            print("-----------------------------------")
            print("0"+w+"# Sending " + text)
            message.send_keys(text)
            message.send_keys(Keys.ENTER) 
          elif userchoice.lower() == 'md':
            print("-----------------------------------")
            print("0"+w+"# Sending " + messagesx[z],text)
            message.send_keys(Keys.ENTER)
            message.send_keys(messagesx[z],text)



        if True:
            #self.driver.close()
            #os.system('cls')
            print("-----------------------------------")
            print("")
            totaltime = time() - start
            print("Done ! " "\n" + str(num) +" Messages has been sent.")
            print("")
            print("process took :",int(totaltime),"seconds")
            print("")
sender = InstagramText()
sender.login()
sender.Sender()

                     

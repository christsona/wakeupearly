#Created by Gerardo Soto
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import datetime
import time
# import tkinter as tk

# driver = webdriver.Firefox('/Users/federaltax/Documents/development/drivers/chromedriver)
#

#enter username here
username = "" 

#enter password here
password = ""
def runner():
   # driver = webdriver.Chrome('C:\drivers\chromedriver.exe')
   path = "/Users/federaltax/Documents/development/drivers/chromedriver"
   driver = webdriver.Chrome(path)
   driver.set_page_load_timeout("10")

# Download geckodriver or chromedriver
   driver.get("https://login.berea.edu/")
   driver.find_element_by_name("j_username").send_keys(username)
   driver.find_element_by_name("j_password").send_keys(password)
   driver.find_element_by_name("_eventId_proceed").click()
   time.sleep(3)
   driver.find_element_by_partial_link_text("Send Me a Push").click()
   time.sleep(3)
   driver.find_element_by_partial_link_text("myBerea").click()
   time.sleep(8)
   driver.find_element_by_partial_link_text("Add or Drop Classes").click()
   time.sleep(2)
   # driver.find_element_by_partial_link_text("Summer 2019").click()
   driver.switch_to.window(driver.window_handles[1])
   driver.find_element_by_xpath("/html/body/div[3]/form/input").click()
   time.sleep(1)
   driver.find_element_by_id("crn_id1").click()
   ActionChains(driver) \
       .send_keys("00000") \
       .key_down(Keys.TAB) \
       .send_keys("00000") \
       .key_down(Keys.TAB) \
       .send_keys("00000") \
       .key_down(Keys.TAB) \
       .send_keys("00000") \
       .key_down(Keys.TAB) \
       .send_keys("00000") \
       .perform()
   driver.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()

   time.sleep(30)
# driver.find_element_by_name("pin").send_keys("837192")


# driver.find_element_by_partial_link_text("Submit").click()
# 837192
#
# CRN_IN


# time.sleep(10)



# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app =Application(master=root)
# app.mainloop()

def main():
   runner()

main()

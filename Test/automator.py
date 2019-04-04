#Created by Gerardo Soto
# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime
import time
import tkinter as tk
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Firefox('C:\Drivers\geckodriver.exe')
#
def runner():
   # driver = webdriver.Chrome('C:\drivers\chromedriver.exe')
   path = "C:\Drivers\chromedriver.exe"
   driver = webdriver.Chrome(path)
   driver.set_page_load_timeout("10")

# Download geckodriver or chromedriver
   driver.get("https://cc-lp5cas-vm.berea.edu/cas-web/login?service=https%3A%2F%2Flp5portal.berea.edu%2Fc%2Fportal%2Flogin")
   driver.find_element_by_name("username").send_keys("username")
   driver.find_element_by_name("password").send_keys("password")
   driver.find_element_by_name("submit_form").click()
   time.sleep(1)
   driver.find_element_by_partial_link_text("Academics").click()
   time.sleep(1)
   driver.find_element_by_partial_link_text("Add or Drop Classes").click()
   time.sleep(1)
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

from selenium import webdriver

class glog:
 def __init__(self,driver):
  self.driver = driver
 def signin(self,usn,pwd):
  self.driver.find_element_by_id("identifierId").send_keys(usn)
  self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
  self.driver.find_element_by_name("password").send_keys(pwd)
  self.driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()



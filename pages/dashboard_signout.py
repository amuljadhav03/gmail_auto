class glogout:
 def __init__(self,driver):
  self.driver = driver
 def signout(self):
  self.driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div/div/a").click()
  self.driver.find_element_by_xpath("//*[@id='gb_71']").click()
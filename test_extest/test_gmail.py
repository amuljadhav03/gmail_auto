from pages.login import glog
from data.userdata import *
from pages.dashboard_signout import glogout
import pytest
@pytest.mark.usefixtures("test_navi")
class TestGmail:
 def test_1(self):
     driver = self.driver
     lp = glog(driver)
     lp.signin(USERNAME,PASSWORD)

 def test_2(self):
     driver = self.driver
     dash = glogout(driver)
     dash.signout()
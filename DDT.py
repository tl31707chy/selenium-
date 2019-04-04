from page.login_page import Login_url,Login
from Common.Base.base import browser
from time import sleep
import unittest
import ddt
test_data=[{"username": "18782048160", "password": "admin123"},
           {"username": "13982500000", "password": "admin123"},
           ]

@ddt.ddt
class login(unittest.TestCase):

    def setUp(self):
        self.driver=browser()
        self.driver.get(Login_url)
        self.driver.maximize_window()
        self.XieFun=Login(self.driver)

    @ddt.data(*test_data)
    def test1(self, data):
        self.XieFun.username(data['username'])
        self.XieFun.password(data['password'])
        self.XieFun.button()

    def tearDown(self):
        sleep(2)
        self.driver.quit()
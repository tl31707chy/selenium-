from appium import webdriver
from time import sleep
import xlrd
import unittest
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {'platformName': 'Android',
                        'deviceName': '127.0.0.1:62001',
                        'platformVersion': '23',
                        'appPackage': 'com.bingfor.wxh',
                        'appActivity': 'com.bingfor.wxh.users.activities.MainActivity',
                        'unicodeKeyboard': True,
                        'reseKeyboard': True}
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.keyevent(4)
        cls.driver.keyevent(4)
        cls.driver.quit()
    def test1(self):
        '''测试登录功能'''
        sleep(4)
        self.driver.keyevent(4)#点击取消定位
        sleep(3)
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()#点击我的
        sleep(2)
        #进入我的模块下
        data2 = self.driver.find_element_by_id("com.bingfor.wxh:id/btnLogin").text
        write = open("D:\\圈子精选\\login-quit\\打印log\\test_report.txt", mode="w")
        print("test1----测试登录功能",file=write)
        print("切换到我的模块==>", data2, file=write)
        self.driver.find_element_by_id("com.bingfor.wxh:id/btnLogin").click()#点击登录/注册
        sleep(2)
        #进入登录界面
        data3 = self.driver.find_element_by_id("com.bingfor.wxh:id/titleTv").text
        print("进入登陆页面==>", data3, file=write)
        data = xlrd.open_workbook('D:\\圈子精选\\login-quit\\用户名密码.xlsx')
        sheet = data.sheets()[0]
        for i in range(1, sheet.nrows):
           print(sheet.row_values(i),file=write)
           self.driver.find_element_by_name("请输入手机号").send_keys(int(sheet.row_values(i)[0]))#输入手机号
           self.driver.find_element_by_id("com.bingfor.wxh:id/tv_pwd").send_keys(int(sheet.row_values(i)[1]))#输入密码
           sleep(2)
           self.driver.find_element_by_name("登录").click()#点击登录
           sleep(3)
           fengsi=self.driver.find_element_by_xpath("//android.widget.TextView[@text='粉丝：']").get_attribute('name')
           n=1
           if fengsi=='粉丝：':
               n=n+1
               print('第'+str(n)+'次登录成功',file=write)
           else:
               print('第'+str(n)+'次登录失败',file=write)
           sleep(3)
           self.driver.find_element_by_id('com.bingfor.wxh:id/btnSetting').click()  # 点击设置
           self.driver.find_element_by_id('com.bingfor.wxh:id/btnLoginOut').click()  # 点击退出登陆
           self.driver.find_element_by_id('com.bingfor.wxh:id/btn_confirm').click()  # 点击确定
           sleep(3)
           other=self.driver.find_element_by_id('com.bingfor.wxh:id/loginTvCenter').get_attribute('name')
           login=other[2:6]
           if login=='登录方式':
               print('第'+str(n)+'次退出成功\n',file=write)
           else:
               print('第'+str(n)+ '次退出失败\n', file=write)








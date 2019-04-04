from selenium import  webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def browser(browser='Chrome'):
    '''打开浏览器，进行判断'''
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("没有发现你所使用的浏览器,你可以使用'firefox','chrome', 'ie' 或者 'phantomjs'")
    except Exception as e:#捕获所有异常的方方法
        print("%s" % e)

class Base(object):
    '''selenium二次封装'''

    def __init__(self,driver):
        '''启动浏览器参数化，默认启动谷歌'''
        self.driver=driver
        self.timeout=2#加载2s,若2s内为加载完成，跑出超时异常
        self.t=0.5#每0.5s查找一次元素

    def find_element(self,locator):
        '''定位到元素返回元素对象，没定位到元素返回timeout异常'''
        element=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator):
        '''定位一组元素'''
        try:
           elements=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
           return elements
        except:
            return []

    def sendKeys(self,locator,text):
        element=self.find_element(locator)
        element.send_keys(text)

    def click(self,locator):
        element = self.find_element(locator)
        element.click()

    def clear(self,locator):
        element=self.find_element(locator)
        element.clear()

    def is_Selected(self,locator):
        '''判断下拉框或者按钮元素是否被选中，返回bool值'''
        element=self.find_element(locator)
        result=element.is_selected()
        return result

    def is_ElementExist(self,locator):
        '''判定元素是否存在'''
        try:
            self.find_element(locator)
            return True
        except:
             return False

    def is_ElementExists(self,locator):
        '''判断一组元素有几个存在   type="radio"   selected   type="radio"'''
        elements = self.find_elements(locator)
        n = len(elements)
        if n == 0:
            return False
        elif n == 1:
               return True
        else:
            print('可定位到元素的个数:%s' % n)
            return True
    def is_title(self,title):
        '''判断标题(完全)，返回bool值'''
        try:
           result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(title))
           return result
        except:
            return False

    def is_title_contains(self,title):
        '''判断标题（包含），返回bool值'''
        try:
           result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
           return result
        except:
            return False

    def is_text_in_element(self,locator,text):
        '''判断文本是否在元素中'''
        try:
           result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,text))
           return result
        except :
            return  False

    def is_value_in_element(self,locator,value):
        '''判断元素value值，返回bool值，空字符串返回false'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

if __name__ == '__main__':
    driver=browser()
    driver.get('http://127.0.0.1:81/zentao/user-login.html')
    zentao=Base(driver)
    loc_username=('id','account')
    loc_password=('name','password')
    loc_submit=('id','submit')
    zentao.sendKeys(loc_username,'admin')
    sleep(1)
    zentao.clear(loc_username)
    sleep(1)
    zentao.sendKeys(loc_username, 'admin')
    zentao.sendKeys(loc_password,'123456')
    zentao.click(loc_submit)








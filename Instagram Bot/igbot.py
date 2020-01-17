from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys



class instaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        self.username = username
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Melde dich an')]") \
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]") \
            .click()
        sleep(2)

    def get_info(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)) \
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]") \
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]") \
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        me_not_following = [user for user in followers if user not in following]
        print("Profiles that follow me and I'm not following them back: ")
        print(me_not_following)
        print("Profiles that don't follow me back: ")
        print(not_following_back)

    def _get_names(self):
        sleep(2)

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")

        last_ht, ht = 0, 1
        while last_ht != ht:
             last_ht = ht
             sleep(2)
             ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button") \
            .click()
        return names

with open('pw.txt','r') as file:
    pw = file.read()

myBot=instaBot('dzudzudzu',pw)
myBot.get_info()

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox(executable_path = 'C:/Users/olegb/Downloads/geckodriver-v0.26.0-win64/geckodriver.exe')	

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(3)
		email = bot.find_element_by_name('username').send_keys(self.username)
		password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)

		time.sleep(3)

	def searchHashtag(self,hashtag):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/tags/' + hashtag)

	def likePhotos(self,amount):
		bot = self.bot

		bot.find_element_by_class_name('v1Nh3').click()

		i = 1
		while i <= amount:
			time.sleep(1)
			bot.find_element_by_class_name('fr66n').click()
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			time.sleep(5)

			i += 1


#insta = InstagramBot('olegbogoslavec123@gmail.com', 'Spring2014')
insta = InstagramBot('vtav2008@gmail.com', 'Spring2020!')
insta.login()
insta.searchHashtag('neutralaesthetic')
insta.likePhotos(40)


#https://ingramer.com/tools/instagram-top-hashtags/
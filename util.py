from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class InstagramBot:
    def __init__(self):
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=tr')
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.managed_default_content_settings.images": 2
        }
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")

        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        version = driver.capabilities['browserVersion']
        print(version)
        return driver

    def login_facebook(self, my_username, my_password):
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        username.send_keys(my_username)
        password.clear()
        password.send_keys(my_password)
        time.sleep(3)
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    def get_instagram_main_page(self):
        self.driver.get('https://www.instagram.com/')
        self.login_facebook("WilliamPhillips8823135", "d6e5Gijg43")
        time.sleep(5)

    def search_page(self, text):
        try:
            # Locate and click the search button
            search_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Ara']"))
            )
            search_button.click()
            time.sleep(3)
            action = ActionChains(self.driver)
            for letter in text:
                action.send_keys(letter)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(3)

            element = self.driver.find_element(By.CSS_SELECTOR, "a.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
                                                                 
            element.click()
        except Exception as e:
            print(f"Error: {e}")

# Example usage:
# instagram_bot = InstagramBot()
# instagram_bot.get_instagram_main_page()

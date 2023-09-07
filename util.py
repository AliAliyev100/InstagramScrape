from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
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

    def get_posts(self):
        all_posts_selector = "div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1" 
        all_posts = self.get_elements_with_css_selector(all_posts_selector, 0)[1]
        posts_selector = "div._aabd._aa8k._al3l"
        posts = self.get_elements_with_css_selector(posts_selector,0,all_posts)
        return posts
    
    def get_posts_data(self, start_post_index = 0, limit = 12):
        posts = self.get_posts()[start_post_index:start_post_index + limit]
        for index, post in enumerate(posts):
            print("Post no: ", index+1)
            self.get_post(post)
            if (index + 1) % 3 == 0:
                post_height = post.size['height']
                self.scroll_page(1,post_height)

    def get_post(self, post):
        first_post_selector = "a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd"
        first_post = self.get_elements_with_css_selector(first_post_selector,0,post)[0]
        time.sleep(1)
        post_url = first_post.get_attribute("href")
        self.hover_element(first_post)
        post_comments_count = self.get_post_comments()
        time.sleep(3)
        self.click_element(first_post)

        post_content = self.get_post_content()
        post_likes_count = self.get_post_likes()
        post_date = self.get_post_date()

        print({
            "url": post_url,
            "content": post_content,
            "likes": post_likes_count,
            "comments": post_comments_count,
            "date": post_date
        })
        print('\n')

        time.sleep(10)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


    def get_post_content(self):
        content_selector = "h1._aacl._aaco._aacu._aacx._aad7._aade"
        content = self.get_elements_with_css_selector(content_selector,0)[0]
        return content.text
    
    def get_post_likes(self):
        likes_selector = "span.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
        likes_count = self.get_elements_with_css_selector(likes_selector,0)[0]
        cleaned_like_count = likes_count.text.replace(" beğenme", "").replace(".", "")
        likes = int(cleaned_like_count)
        return likes

    def get_post_comments(self):
        comments_selector = "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xl565be.x1xlr1w8.x9bdzbf.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
        comments = self.get_elements_with_css_selector(comments_selector,0)[1]
        cleaned_comments_string = comments.text.replace(".", "").strip()
        comments = int(cleaned_comments_string)
        return comments

    def get_post_date(self):
        date_selector = "time._aaqe"
        format_string = "%Y-%m-%dT%H:%M:%S.%fZ"

        date_element = self.get_elements_with_css_selector(date_selector,0)[0]
        date_string = date_element.get_attribute("datetime")
        parsed_datetime = datetime.strptime(date_string, format_string)

        return parsed_datetime



    def get_post_url(self, post):
        url_selector = ""
        url = self.get_elements_with_css_selector(url_selector,0,post)[0]
        return url.text

    def get_elements_with_css_selector(self, selector, startIndex=0, driver=None):
        if driver is None:
            driver = self.driver 
        posts = driver.find_elements(By.CSS_SELECTOR, selector)[startIndex:]
        return posts

    def click_element(self, element):
        if(self.is_element_visible(element)):
            self.driver.execute_script("arguments[0].click();", element)

    def is_element_visible(self,element):
        try:
            return element.is_displayed()
        except StaleElementReferenceException:
            return False
        
    def hover_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def scroll_page(self, num_scrolls=1, scroll_amount=1810):
        for i in range(num_scrolls):
            scroll_total = (i + 1) * scroll_amount
            current_y = self.driver.execute_script("return window.pageYOffset;")
            self.driver.execute_script(f"window.scrollTo(0, {current_y + scroll_total});")
            time.sleep(3)
            
            new_y = self.driver.execute_script("return window.pageYOffset;")
            if new_y == current_y:
                return False 
        
        return True 
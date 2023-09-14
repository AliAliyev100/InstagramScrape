import time
from util import InstagramBot

instagram_bot = InstagramBot()
instagram_bot.get_instagram_main_page()
instagram_bot.get_post_comments("https://www.instagram.com/p/CxGevRKpfi6/")
time.sleep(5000)

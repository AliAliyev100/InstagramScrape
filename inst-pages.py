import time
from util import InstagramBot

instagram_bot = InstagramBot()
instagram_bot.get_instagram_main_page()
instagram_bot.search_page("porsche")
time.sleep(10)
instagram_bot.get_posts_data(start_post_index=0, limit=12)

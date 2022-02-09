import time
import config
from instapy import InstaPy, smart_run

# Login credentials from config file
username = config.insta_username
password = config.insta_password
tags = config.tags

# Instapy session
session = InstaPy(username=username, password=password, headless_browser=False)

with smart_run(session):
    session.login()
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, potency_ratio=-1.10, max_followers=20000,
                                    min_followers=100, min_following=100, min_posts=6)
    # session.set_dont_include(friends)
    session.set_simulation(enabled=False)
    session.set_skip_users(skip_private=True, skip_no_profile_pic=True, skip_business=True)
    session.set_do_like(enabled=True, percentage=100)
    session.set_dont_like(["naked", "nsfw", "beef", '#beef', "gun", "#raw"])
    session.set_do_follow(enabled=True, percentage=70, times=1)
    session.set_smart_hashtags()
    session.set_action_delays(enabled=True, like=10, follow=15, unfollow=12, randomize=True)

    # Like by given tags
    session.like_by_tags(tags, amount=6, use_smart_hashtags=True)
    time.sleep(10)
    # Like post within feed
    session.like_by_feed(amount=4, randomize=True, unfollow=False, interact=True)
    time.sleep(15)

    # Unfollow the earliest
    session.set_dont_unfollow_active_users(enabled=True, posts=1)
    session.unfollow_users(amount=2, instapy_followed_enabled=True,
                           style="LIFO", unfollow_after=42*60*60, sleep_delay=120)
    session.end()


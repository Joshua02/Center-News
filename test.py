# import all necessary things
import re
from os import replace

# facebook info
f = open('facebook.txt', 'r')
facebook = f.readlines()
f.close()
while '\n' in facebook:
    facebook.remove('\n')

username = facebook.pop(0)
password = facebook.pop(0)

from facebook import fb_all_posts

posts = fb_all_posts(facebook, username, password, 8)
posts = sorted(posts, key = lambda _: _['datetime_obj'], reverse=True)
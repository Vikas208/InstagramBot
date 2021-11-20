from instabot import Bot, bot
import os
import glob
from tqdm.std import tqdm
password_file = open('password.txt', 'r')
password = password_file.read()
user_file = open('username.txt','r')
user_name = user_file.read()
bot = Bot(max_follows_per_day=150, follow_delay=180, filter_previously_followed=True,
          filter_business_accounts=True, filter_verified_accounts=True, filter_private_users=True)

bot.login(username=user_name, password=password)

user_list = ['therock', 'cristiano', 'leomessi',
             'neeraj____chopra', 'thecodercoder', 'mevidyutjammwal', 'kiaraaliaadvani', 'neymarjr']

for user in user_list:
    medias = bot.get_user_medias(user, filtration=False)
    print(medias)

    for i in range(0, 2):
        likers = bot.get_media_likers(medias[i])
        cnt = 0
        for liker in tqdm(likers):
            if cnt < 10:
                print(bot.get_username_from_user_id(liker))
                bot.follow(liker)
                cnt += 1

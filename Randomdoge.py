import time
import praw
import random
#Credit- Thanks to /u/spacer0cket for all his help! He cleaned up the code and  added some great new features.
r = praw.Reddit('Randomactofdogebot')
r.login("USERNAME","PASSWORD")
already_done = set()
prawWords = ['a', 'e', 'i', 'o', 'u']
#And sometimes Y. Including all the vowels makes the bot more random.
prawTerms = ['+/u/dogetipbot']

amount_min = 15
amount_max = 25


#Returns amount between 2 numbers, as an integer. Default 15--25
def rand_amount(minimum, maximum):
    return random.randint(minimum, maximum)

#Find comment to tip
def pick_random_comment():
    global amount_min
    global amount_max
    
    subreddit = r.get_subreddit('dogecoin')
    subreddit_comments = subreddit.get_comments(limit=200)
    for comment in subreddit_comments:
        op_text = comment.body
        has_praw = any(string in op_text for string in prawWords)
        if comment.id not in already_done and has_praw:
            comment.reply('This is a random act of doge! +/u/dogetipbot ' + str(rand_amount(amount_min, amount_max)) + ' doge\n\nPlease consider tipping this bot to keep it running!\n\n[Bot Info](http://www.reddit.com/r/dogecoin/comments/1yi0s1/all_the_information_you_need_to_know_about_me/) ---- [Source Code](https://github.com/Healdb/random_act_of_doge_bot)')
            already_done.add(comment.id)
            break

#Look for incoming tip
def check_inbox():
    messages = r.get_unread('comments')
    for message in messages:
        op_text = message.body
        has_praw = any(string in op_text for string in prawTerms)
        if message.id not in already_done and has_praw:
            message.reply('Thank you! This will help to keep me running!\n\n[Bot Info](http://www.reddit.com/r/dogecoin/comments/1yi0s1/all_the_information_you_need_to_know_about_me/) ---- [Source Code](https://github.com/Healdb/random_act_of_doge_bot)')
            already_done.add(message.id)
            break



while True:
    check_inbox()
    pick_random_comment()
    time.sleep(3600)

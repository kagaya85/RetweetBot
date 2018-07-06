import tweepy
import random
import KeysAndTokens as kt
import datetime
from qqbot import qqbotsched

screen_name = 'KanColle_STAFF'
auth = tweepy.OAuthHandler(kt.consumer_key, kt.consumer_secret)
auth.set_access_token(kt.access_token, kt.access_token_secret)
api = tweepy.API(auth, proxy='127.0.0.1:xxxx')

alltweets = []
groupList = []
oldest_id = 0

def onStartupComplete(bot):
    global oldest_id
    global groupList
    new_tweets = api.user_timeline(screen_name, count = 5, tweet_mode="extended")
    alltweets.extend(new_tweets)
    oldest_id = alltweets[0].id
    groupList = bot.list('group')

def onUpdate(bot, tinfo):
    global groupList
    if tinfo == 'group':
        groupList = bot.list('group')

@qqbotsched(hour='0-23/1', minute='0-59/1')
def mytask(bot):
    """
        定时任务
    """
    global oldest_id

    try:
        new_tweets = api.user_timeline(screen_name, count = 5, tweet_mode="extended", since_id = oldest_id)
        if len(new_tweets) > 0:
            alltweets.extend(new_tweets)
            if len(new_tweets) > 1:
                oldest_id = new_tweets[0].id
            else:
                oldest_id = new_tweets.id

            if len(groupList) > 0:
                # 发送给所有群
                for each in groupList:
                    for tweet in new_tweets:
                        bot.SendTo(each, 'time: {}\n{}'.format(tweet.created_at, tweet.full_text))
            # 发送给好友
            friend = bot.List('buddy', 'Ta')
            if friend:
                f = friend[0]
                for tweet in new_tweets:
                    bot.SendTo(f, 'time: {}\n{}'.format(tweet.created_at, tweet.full_text))
    except Exception as err:
        friend = bot.List('buddy', 'Ta')
        if friend:
            f = friend[0]
            bot.SendTo(f, err)


def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member) == False:
        if contact.ctype == 'buddy':
            if content == 'check':
                bot.SendTo(contact, "time: {}\n{}".format(alltweets[0].created_at, alltweets[0].full_text))
            elif content == 'hi':
                bot.SendTo(contact, "Hello！アメリカ生まれの大型正規空母Saratogaです。歴史深い由緒ある名前を頂いています。あの大きな戦いでは、最初から最後まで頑張ったんです。")
            elif content == '--stop':
                bot.SendTo(contact, 'closed')
                bot.Stop()
            # elif content == '--list':
            #     bot.SendTo(contact, bot.List('buddy'))
            else:
                bot.SendTo(contact, reply())
        elif(contact.ctype == 'group'):
            if '@ME' in content and 'check' in content:
                bot.SendTo(contact, "time: {}\n{}".format(alltweets[0].created_at, alltweets[0].full_text))
            elif '@ME' in content and 'hi' in content:
                bot.SendTo(contact, "Hello！アメリカ生まれの大型正規空母Saratogaです。歴史深い由緒ある名前を頂いています。あの大きな戦いでは、最初から最後まで頑張ったんです。")
            elif '@ME' in content:
                bot.SendTo(contact, reply())
            elif '现在几点' in content:
                bot.SendTo(contact, "It is {} now".format(datetime.datetime.now().strftime('%H:%M')))
            else:
                pass
        else:
            pass
        


def reply():
    text = [
        "航空母艦、Saratogaです。提督、サラとお呼びくださいね。よろしくお願い致します。",
        "How are you?",
        "航空母艦Saratoga抜錨します。続いて",
        "Oh my god…",
        "はい、サラはここに~",
        "んんん。。。やはりかがやさんのことが大好きだよ～",
        "花Q！"
    ]

    return random.choice(text)



# if __name__ == "main":
#     alltweets = []

#     new_tweets = api.user_timeline(screen_name, count = 5, tweet_mode="extended")

#     alltweets.extend(new_tweets)

#     oldest = alltweets[0].id - 1

#     for tweet in alltweets:
#         print("id: {}".format(tweet.id))
#         print(tweet.full_text)


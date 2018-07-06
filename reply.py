import json
import random
import datetime

replyList = {}

def init_replyList():
    global replyList
    with open("./data/reply.json", 'r', encoding='UTF-8') as f:
        replyList = json.load(f)


def reply(s):
    reply = replyList.get(s)
    if isinstance(reply["content"], list):
        return random.choice(reply["content"])
    else:
        return reply["content"]


def add_reply(s, writer, content):
    newReply = {
            s: {
                "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "writer": writer,
                "content": content
            } 
        }
    replyList.update(newReply)
    return True


def del_reply(s):
    """
        返回值含义：
            0：删除失败，未找到
            1：删除失败，无权限
            2：删除成功
    """
    reply = replyList.get(s)
    if reply == None:
        return 0
    elif reply['writer'] == "administer":
        return 1
    else:
        del replyList[s]
        return 2


def search_reply(s):
    """
        返回对应的dict
        查询不到返回None
    """
    if s in replyList:
        reply = replyList.get(s)
        return reply
    else:
        return None


def save():
    with open("./data/reply.json", 'w', encoding='UTF-8') as f:
        json.dump(replyList, f, ensure_ascii = False, indent = 4)


if __name__ == '__main__':
    init_replyList()
    print("测试回复：")
    s = input("please input:")
    print(reply(s))
    s = input("please input:")
    print(reply(s))
    
    print("测试添加：")
    s = input("please input:")
    content = input("please input content:")
    writer = input("please input writer:")
    if add_reply(s, writer, content) :
        print("add complete!")
    s = input("please input:")
    print(reply(s))
    
    # print("测试查询：")
    # s = input("please input:")
    # print(search_reply(s))
    # s = input("please input:")
    # print(search_reply(s))

    # print("测试删除：")
    # s = input("please input:")
    # print(del_reply(s))

    save_replyList()
    print("test over!")
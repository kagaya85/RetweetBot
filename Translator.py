from googletrans import Translator

translator = Translator()
content = input('please input:')

transFlag = 1
if(len(content) > 200):
    bot.SendTo(contact, "太长不看")
else:
    transFlag = 1
    try:
        if content[2] == '到':
            if content[3:5] == "汉语" or content[3:5] == "中文":
                translations = translator.translate(content[5:].lstrip(), dest='zh-cn')
            elif content[3:7] == "简体中文":
                translations = translator.translate(content[7:].lstrip(), dest='zh-cn')
            elif content[3:5] == "英语":
                translations = translator.translate(content[5:].lstrip(), dest='en')
            elif content[3:5] == "韩语":
                translations = translator.translate(content[5:].lstrip(), dest='ko')
            elif content[3:5] == "日语":
                translations = translator.translate(content[5:].lstrip(), dest='ja')
            elif content[3:5] == "德语":
                translations = translator.translate(content[5:].lstrip(), dest='de')
            elif content[3:5] == "法语":
                translations = translator.translate(content[5:].lstrip(), dest='fr')
            elif content[3:5] == "俄语":
                translations = translator.translate(content[5:].lstrip(), dest='ru')
            elif content[3:7] == "西班牙语":
                translations = translator.translate(content[7:].lstrip(), dest='es')
            elif content[3:7] == "葡萄牙语":
                translations = translator.translate(content[7:].lstrip(), dest='pt')
            elif content[3:7] == "繁体中文":
                translations = translator.translate(content[7:].lstrip(), dest='zh-tw')
            else:
                transFlag = 0
        else:
            translations = translator.translate(content[2:].lstrip(), dest='zh-cn')
        if transFlag:
            bot.SendTo(contact, translations.text)
        else:
            bot.SendTo(contact, "抱歉，我暂时做不到")
    except Exception as err:
        bot.SendTo(contact, "我好像不能理解这个\n{}".format(err))

print(translations.text)
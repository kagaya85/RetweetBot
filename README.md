# RetwitterBot
实现自动转发最新twitter到QQ的机器人  
Retweet newest tweets to QQ by using this bot, which based on tweepy and QQbot.   
Just make more convenience for people in our daily life (*^_^*)  

**感谢[azuse](https://github.com/azuse)提供的代理服务**

### 施工中………………

## 基本功能
### 2018年7月4日更新
1. 实现基本的转推功能，可以将最新的tweet转发到qq群中
2. 实现简单的回复功能：私聊或者在群中check数字（无空格）可查看最新的某条tweet  
3. 私聊时若无设定匹配语句则会随机选择一条回复语句，目前匹配语句：hi、现在几点、check

### 2018年7月5日更新  
1. 考虑加入googleAPI实现更多功能
2. 加入学习功能：在群中回复“学习A回答B”即可让机器人在群中接受到消息A后自动回复B
3. 还未加入对表情字符的判定，存在bug
4. 查询/删除 + 对应关键字可实现对应功能

### 2018年7月7日更新
1. 修复了无法处理被qq表情的bug
2. 加入了google翻译功能，回复 翻译+文字 默认翻译到简体中文，回复 翻译到+语言+文字 可翻译到对应语言
3. 修复了转推时间错误的bug

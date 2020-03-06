# Link2Telegram

一个简单的 Telegram 机器人。

已经实现的：可以输入链接，输出到指定频道中

## 使用方法

新建一个 `telebot_setting.py`，有关该文件的格式可以查看[这里](#文件格式)，将机器人的 `TOKEN` 填入。该机器人暂时只支持推送到频道中（当然把某行代码取消注释就可以直接推送到机器人中了）。

``` code
/link xxxx
```

其中 xxx 为文章链接，如 `https://mp.weixin.qq.com/s/bh9L96kojio7ZWYYRr4nAw` 之类的格式。

### 频道

想要让机器人直接推送到频道中，需要将机器人设置为管理员，并将频道中的任意一条消息转发到机器人中，从而获得 `chat_id`。之后设置 `telebot_setting.py` 中的 `CHAT_ID` 参数即可。

## 文件格式

`telebot_setting.py`：

``` python
TOKEN = xxxxxx
CHAT_ID = xxxxxx
```

## 期望

支持将微信文章的格式优雅地转换为 Telegraph 格式。

**为什么要实现这样一个机器人？**

因为有的时候在微信上看见了不错的文章，想要保存下来，但是微信原本的格式太难受了，就想到保存在 Telegraph 上。但是由于自己太菜，不能将微信文章的格式优雅地转换为 Telegraph 的格式，因此先实现这样一个机器人，直接链接到 Telegram 上。

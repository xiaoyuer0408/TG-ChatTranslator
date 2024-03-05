安装依赖
在使用前，您可能需要安装以下依赖：
pip install aiohttp telethon
如果您的机器上还缺少其他依赖，请自行安装。
使用方法
在config.json中配置真实的api_id和api_hash，这些可以从https://my.telegram.org/apps申请获得。
执行脚本，登录您的账号。
使用对应账号在对应聊天群里设置启用/禁用。
指令
.tt-off：群内直接输入，禁用本账号/频道号在该聊天/群的翻译功能。
.tt-on,zh,zh|en|ru：设置并开启本账号/频道号在该聊天/群的翻译功能。参数依次是：源语言，目标语言列表。目标语言列表将按顺序显示，第一个语言作为主要语言。如果在目标语言列表中不包含原语言，则相当于上版本的不保留原内容。目标语言列表使用|隔开。
以上配置会实时写进配置文件，后续重启脚本都会加载。

注意：该服务跑在国外服务器上效果会更佳！

支持的语言列表
源语言
AR - Arabic
BG - Bulgarian
CS - Czech
...
ZH - Chinese
目标语言
AR - Arabic
BG - Bulgarian
CS - Czech
...
ZH - Chinese (simplified)
注：原创：Linux.do 自己小小的修改了一下。

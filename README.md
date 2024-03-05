使用前可能需要安装依赖：
pip install aiohttp telethon
如果你本机还缺其他依赖，自行安装即可。

使用方法：
在config.json中配置真实的api_id和api_hash，申请自https://my.telegram.org/apps
执行脚本，登录你的账号。
使用对应账号在对应聊天群里设置启用/禁用。
指令：
.tt-off 群内直接输入，禁用本账号/频道号在该聊天/群的翻译功能。

.tt-on,zh,zh|en|ru 设置并开启本账号/频道号在该聊天/群的翻译功能。参数依次是：源语言，目标语言列表。

目标语言列表将按顺序显示，第一个语言作为主要语言。
如果在目标语言列表中不包含原语言，则相当于上版本的不保留原内容。
目标语言列表使用|隔开。

以上配置会实时写进配置文件，后续重启脚本都会加载。

该服务跑在国外服务器上效果会更佳！

 附：deepl的源语言和目标语言列表
源语言
AR - Arabic
BG - Bulgarian
CS - Czech
DA - Danish
DE - German
EL - Greek
EN - English
ES - Spanish
ET - Estonian
FI - Finnish
FR - French
HU - Hungarian
ID - Indonesian
IT - Italian
JA - Japanese
KO - Korean
LT - Lithuanian
LV - Latvian
NB - Norwegian (Bokmål)
NL - Dutch
PL - Polish
PT - Portuguese (all Portuguese varieties mixed)
RO - Romanian
RU - Russian
SK - Slovak
SL - Slovenian
SV - Swedish
TR - Turkish
UK - Ukrainian
ZH - Chinese
目标语言：
AR - Arabic
BG - Bulgarian
CS - Czech
DA - Danish
DE - German
EL - Greek
EN - English (unspecified variant for backward compatibility; please select EN-GB or EN-US instead)
EN-GB - English (British)
EN-US - English (American)
ES - Spanish
ET - Estonian
FI - Finnish
FR - French
HU - Hungarian
ID - Indonesian
IT - Italian
JA - Japanese
KO - Korean
LT - Lithuanian
LV - Latvian
NB - Norwegian (Bokmål)
NL - Dutch
PL - Polish
PT - Portuguese (unspecified variant for backward compatibility; please select PT-BR or PT-PT instead)
PT-BR - Portuguese (Brazilian)
PT-PT - Portuguese (all Portuguese varieties excluding Brazilian Portuguese)
RO - Romanian
RU - Russian
SK - Slovak
SL - Slovenian
SV - Swedish
TR - Turkish
UK - Ukrainian
ZH - Chinese (simplified)


注：原创：https://linux.do/t/topic/18308?u=nextstrain 自己小小的修改了一下。

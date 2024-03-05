# ChatTranslator

## 🌌 引子
 "实时翻译，沟通无障碍。"

![ChatTranslator](https://img.shields.io/badge/ChatTranslator-TranslationTool-blue)

ChatTranslator是一个实时聊天翻译工具，旨在帮助用户跨语言进行通信。支持多种语言实时互译，适用于Telegram聊天群。

### 技术栈
Python3.8及以上, aiohttp, Telethon

### 功能特性
- 实时聊天翻译
- 支持多种源语言和目标语言
- 用户可以通过特定指令在聊天群中启用或禁用翻译功能

### 安装指南
安装项目依赖：

pip install aiohttp telethon

安装任何其他可能缺失的依赖。

### 使用方法
1. 配置config.json文件，包括获取api_id和api_hash。
2. 执行脚本并登录账号。
3. 在聊天群里使用`.tt-off`和`.tt-on`指令来禁用或启用翻译功能。

### 指令说明
- `.tt-off`：禁用翻译功能
- `.tt-on,zh,zh|en|ru`：启用翻译功能，设置源语言和目标语言列表

### 配置文件
配置会实时写入config.json文件，并在重启脚本时加载。

### 注意事项
该服务在国外服务器上运行效果更佳。

### 支持的语言列表
#### 源语言
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

#### 目标语言
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


_________________

## 🍁 致谢
- 脚本原创[Linux.do](https://linux.do/t/topic/18308?u=nextstrain)，

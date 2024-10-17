# -*- coding: utf-8 -*-

import asyncio
import json
import logging
import os
import time

import aiohttp
from telethon import events
from telethon.sync import TelegramClient

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

async def load_config():
    if not os.path.exists('config.json'):
        logging.error('config.json not found, creating an empty one')
        with open('config.json', 'w') as f:
            json.dump({}, f)  # 创建一个空的配置文件
        exit()

    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

async def save_config(cfg, target_config):
    cfg['target_config'] = target_config
    with open('config.json', 'w') as f:
        json.dump(cfg, f, indent=2)

async def translate_response(response):
    if response.status != 200:
        logging.error(f"翻译失败：{response.status}")
        raise Exception(f"翻译失败")

    result = await response.json()
    if result['code'] != 200:
        logging.error(f"翻译失败：{result}")
        raise Exception(f"翻译失败")

    return result['data']

async def translate_single(text, source_lang, target_lang, session):
    if source_lang == target_lang:
        return target_lang, text

    url = "https://api.deeplx.org/hnAG7ZM_46Ld4zIlsvZCvKSxlcorDm7bHl7yHN0as1E/translate"  # 请替换为实际的翻译API URL
    payload = {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }

    start_time = time.time()
    async with session.post(url, json=payload) as response:
        logging.info(f"翻译从 {source_lang} 至 {target_lang} 耗时: {time.time() - start_time}")
        result = await translate_response(response)

        return target_lang, result

async def translate_text(text, source_lang, target_langs, session) -> {}:
    result = {}
    tasks = [translate_single(text, source_lang, target_lang, session) for target_lang in target_langs]
    translations = await asyncio.gather(*tasks)
    for lang, text in translations:
        result[lang] = text
    return result

async def handle_command(event, target_key, text, target_config):
    if text == '.tt-off':
        await event.delete()

        if target_key in target_config:
            del target_config[target_key]
            await save_config(cfg, target_config)
            logging.info("已禁用: %s" % target_key)

        return False

    if text.startswith('.tt-on,'):
        await event.delete()

        _, source_lang, target_langs = text.split(',')
        target_config[target_key] = {
            'source_lang': source_lang,
            'target_langs': target_langs.split('|')
        }

        await save_config(cfg, target_config)
        logging.info(f"设置成功: {target_config[target_key]}")

        return False

    return True

async def handle_message(event, cfg, target_config):
    target_key = '%d.%d' % (event.chat_id, event.sender_id)
    try:
        message = event.message

        if not message.text:
            return

        message_content = message.text.strip()
        if not message_content:
            return

        if message_content.startswith('.tt-') and not await handle_command(event, target_key, message_content, target_config):
            return

        if target_key not in target_config:
            return

        logging.info(f"翻译消息: {message.text}")

        config = target_config[target_key]
        target_langs = config['target_langs']
        if not target_langs:
            return

        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            translated_texts = await translate_text(message.text, config['source_lang'], target_langs, session)
            logging.info(f"翻译耗时: {time.time() - start_time}")

            modified_message = translated_texts[target_langs[0]]

            if len(target_langs) > 1:
                secondary_messages = []
                for lang in target_langs[1:]:
                    secondary_messages.append(translated_texts[lang])

                modified_message += '\n```%s\n```' % '\n'.join(secondary_messages)

            await message.edit(modified_message)
    except Exception as e:
        logging.error(f"Error handling message: {e}")

async def main():
    global cfg
    cfg = await load_config()
    api_id = cfg['api_id']
    api_hash = cfg['api_hash']
    target_config = cfg['target_config'] if 'target_config' in cfg else {}

    client = TelegramClient('chat_translator', api_id, api_hash)

    @client.on(events.NewMessage(outgoing=True))
    async def handle_new_message(event):
        await handle_message(event, cfg, target_config)

    try:
        await client.start()
        await client.run_until_disconnected()
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())

from telethon import TelegramClient
import time

# Настройки
api_id = 123456   # вставь свой api_id
api_hash = "your_api_hash"  # вставь свой api_hash
phone = "+79990000000"  # твой номер телефона
message = "подписывайтесь на https://t.me/mgtstudio"
delay = 5
# Список чатов (ссылки или ID)
chats = [
    "https://t.me/testchat1",
    "https://t.me/testchat2",
    -1001234567890  # можно и ID
]

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    for chat in chats:
        try:
            await client.send_message(chat, message)
            print(f"[+] Сообщение отправлено в {chat}")
            time.sleep(delay)
        except Exception as e:
            print(f"[-] Ошибка при отправке в {chat}: {e}")

with client:
    client.loop.run_until_complete(main())

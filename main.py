import os, asyncio, sys
from telethon import TelegramClient, events

# تنظیمات از Secrets
API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# ساخت کلاینت با نام سشن جدید برای رفع قفل شدگی
client = TelegramClient('favme_session_new', API_ID, API_HASH)

print("--- STARTING BOT ---")
sys.stdout.flush() # اجبار گیت‌هاب به نمایش لاگ

@client.on(events.ChatAction)
async def group_handler(event):
    try:
        user = await event.get_user()
        if not user or user.bot:
            return

        welcome_text = f"""سلام {user.first_name} عزیز
یه توضیح کوتاه اول کار: این پیام به‌صورت اتوماتیک توسط بات تلگرام و کدهای پایتون ارسال شده، پس اگه جواب ندادم بدون یا آفلاینم یا خوابم یا به تلگرام دسترسی ندارم.

به گروه شخصی من، مهرداد، خوش اومدی.
این که الان اینجایی یعنی احتمالاً یه‌سری سلیقه و علاقه‌ مشترک داریم؛
از فیلم و موسیقی گرفته تا حال‌وهوای روزمره و چیزایی که تو این دنیای مجازی با هم شریک می‌شیم.
امیدوارم تو گروه لحظات خوبی داشته باشی و مطالب به کارت بیاد.

ممنون که هستی.
اگه خودت هم کانال داری، لینکشو همین‌جا بفرست؛
به محض این که خودم (نه ربات) آنلاین بشم، حتماً سر می‌زنم.

اگه دوست داشتی، خودت رو هم معرفی کن.
✨ به گروه 'A Beautiful Mind' خوش اومدی"""

        goodbye_text = "دیدم رفتی، گفتم بگم: چرا؟ 😄\nشوخی شوخی…\nبه‌هرحال ممنون از همراهی‌ت، سلامت باشی."

        if event.user_joined or event.user_added:
            sent_msg = await event.reply(welcome_text)
            await asyncio.sleep(300)
            await sent_msg.delete()

        elif event.user_left:
            sent_msg = await client.send_message(event.chat_id, goodbye_text)
            await asyncio.sleep(300)
            await sent_msg.delete()
    except Exception as e:
        print(f"Error: {e}")

async def main():
    print("Connecting to Telegram...")
    sys.stdout.flush()
    await client.start(bot_token=BOT_TOKEN)
    print("✅ BOT IS ONLINE!")
    sys.stdout.flush()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

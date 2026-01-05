import os, asyncio
from telethon import TelegramClient, events

# دریافت اطلاعات از Secrets گیت‌هاب
API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
CH_ID = 'favme' # آیدی کانال شما بدون @

# راه اندازی ربات با توکن
client = TelegramClient('favme_welcome', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

print("🚀 FavMe Welcome Bot is Running...")

# مدیریت ورود و خروج اعضا
@client.on(events.ChatAction)
async def welcome_manager(event):
    try:
        # وقتی کسی عضو میشه یا ادد میشه
        if event.user_joined or event.user_added:
            user = await event.get_user()
            name = user.first_name if user.first_name else "دوست عزیز"
            
            welcome_msg = (
                f"سلام **{name}** عزیز! ❤️\n\n"
                f"به کانال **FavMe** خیلی خوش اومدی.\n"
                f"اینجا قراره با هم از سد محدودیت‌ها بگذریم و دنیای آزاد اینترنت رو بگردیم. 🛰️\n\n"
                f"امیدوارم محتوای کانال برات مفید باشه! ✨"
            )
            await client.send_message(CH_ID, welcome_msg)
            print(f"✅ پیام خوش‌آمدگویی برای {name} ارسال شد.")

        # وقتی کسی لفت میده
        elif event.user_left:
            user = await event.get_user()
            name = user.first_name if user.first_name else "کاربر"
            
            goodbye_msg = (
                f"حیف شد که از پیشمون رفتی **{name}**... 😢\n"
                f"هر جا هستی موفق باشی. جاده همیشه برای برگشتت بازه! 🌹"
            )
            await client.send_message(CH_ID, goodbye_msg)
            print(f"👋 پیام خداحافظی برای {name} ارسال شد.")

    except Exception as e:
        print(f"❌ ارور: {e}")

# زنده نگه داشتن ربات
client.run_until_disconnected()

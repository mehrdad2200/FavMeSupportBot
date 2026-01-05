import os, asyncio, sys
from telethon import TelegramClient, events
from telethon.errors import ApiIdInvalidError, TokenInvalidError

# تنظیمات
API_ID = os.getenv('API_ID', '')
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# تمیز کردن مقادیر (حذف فاصله‌های احتمالی)
API_ID = int(API_ID.strip()) if API_ID.strip().isdigit() else 0
API_HASH = API_HASH.strip()
BOT_TOKEN = BOT_TOKEN.strip()

client = TelegramClient(None, API_ID, API_HASH)

print("--- STARTING BOT ---")
sys.stdout.flush()

@client.on(events.ChatAction)
async def group_handler(event):
    try:
        user = await event.get_user()
        if not user or user.bot: return

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

        if event.user_joined or event.user_added:
            sent_msg = await event.reply(welcome_text)
            await asyncio.sleep(300)
            await sent_msg.delete()
        elif event.user_left:
            sent_msg = await client.send_message(event.chat_id, "خداحافظ...")
            await asyncio.sleep(300)
            await sent_msg.delete()
    except Exception as e:
        print(f"Error: {e}")

async def main():
    print(f"Checking Connection for API_ID: {API_ID}...")
    sys.stdout.flush()
    try:
        await client.start(bot_token=BOT_TOKEN)
        print("✅ ✅ ✅ BOT IS ONLINE!")
    except ApiIdInvalidError:
        print("❌ ERROR: API_ID or API_HASH is wrong!")
    except TokenInvalidError:
        print("❌ ERROR: BOT_TOKEN is wrong!")
    except Exception as e:
        print(f"❌ UNKNOWN ERROR: {e}")
    
    sys.stdout.flush()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

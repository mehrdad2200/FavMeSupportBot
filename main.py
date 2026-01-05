import os, asyncio
from telethon import TelegramClient, events

# تنظیمات از Secrets گیت‌هاب
API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')

# راه‌اندازی ربات
client = TelegramClient('favme_bot', API_ID, API_HASH)

print("🚀 FavMe Bot is Starting with Full Text...")

@client.on(events.ChatAction)
async def group_handler(event):
    try:
        user = await event.get_user()
        if not user or user.bot:
            return

        # --- متن خوش‌آمدگویی اختصاصی تو ---
        welcome_text = f"""سلام {user.first_name} عزیز

یه توضیح کوتاه اول کار: این پیام به‌صورت اتوماتیک توسط بات تلگرام و کدهای پایتون ارسال شده، پس اگه جواب ندادم بدون یا آفلاینم یا خوابم یا به تلگرام دسترسی ندارم.
خب…

به گروه شخصی من، مهرداد، خوش اومدی.

این که الان اینجایی یعنی احتمالاً یه‌سری سلیقه و علاقه‌ مشترک داریم؛

از فیلم و موسیقی گرفته تا حال‌وهوای روزمره و چیزایی که تو این دنیای مجازی با هم شریک می‌شیم.
امیدوارم تو گروه لحظات خوبی داشته باشی و مطالب به کارت بیاد.

ممنون که هستی.
اگه خودت هم کانال داری، لینکشو همین‌جا بفرست؛

به محض این که خودم (نه ربات) آنلاین بشم، حتماً سر می‌زنم.

اگه دوست داشتی، خودت رو هم معرفی کن.
✨ به گروه 'A Beautiful Mind' خوش اومدی"""

        # --- متن خداحافظی اختصاصی تو ---
        goodbye_text = f"""دیدم رفتی، گفتم بگم: چرا؟ 😄
شوخی شوخی…
به‌هرحال ممنون از همراهی‌ت، سلامت باشی."""

        # اگر کسی وارد شد
        if event.user_joined or event.user_added:
            sent_msg = await event.reply(welcome_text)
            print(f"✅ خوش‌آمدگویی برای {user.first_name} ارسال شد.")
            await asyncio.sleep(300) # انتظار ۵ دقیقه
            await sent_msg.delete()
            print("🗑️ پیام خوش‌آمدگویی پاک شد.")

        # اگر کسی خارج شد
        elif event.user_left:
            sent_msg = await client.send_message(event.chat_id, goodbye_text)
            print(f"👋 خداحافظی برای {user.first_name} ارسال شد.")
            await asyncio.sleep(300)
            await sent_msg.delete()
            print("🗑️ پیام خداحافظی پاک شد.")

    except Exception as e:
        print(f"❌ خطا: {e}")

async def main():
    await client.start(bot_token=BOT_TOKEN)
    
    # قطع کردن بقیه سشن‌ها برای جلوگیری از پیام تکراری
    try:
        await client.sign_out_elsewhere()
    except:
        pass
        
    print("✅ ربات مهرداد آنلاین شد.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

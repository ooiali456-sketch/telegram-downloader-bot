import telebot
from yt_dlp import YoutubeDL
import os

# خلي التوكن مالتك هنا بين الفارزتين
API_TOKEN ='8615192238:AAEUOG6JFuML-QBtLlTz8em-oZ-SqEFwOG8'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل رابط فيديو من تيك توك أو إنستغرام وسأحمله لك.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if "tiktok.com" in url or "instagram.com" in url:
        sent_msg = bot.reply_to(message, "شكرت الله اليوم لان انا بحياتك؟")
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'video.mp4',
                'quiet': True,
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video)

            os.remove('video.mp4')
            bot.delete_message(message.chat.id, sent_msg.message_id)
        except Exception as e:
            bot.edit_message_text(f"حدث خطأ: {e}", message.chat.id, sent_msg.message_id)
    else:
        bot.reply_to(message, "يرجى إرسال رابط صحيح.")


print("البوت بدأ بالعمل الآن...")
bot.polling()
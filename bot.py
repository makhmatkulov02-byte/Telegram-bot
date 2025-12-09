# 1-bosqich  >  Kerakli kutubxonalarni chaqirildi
import os  # Fayllarni o‘chirish, tekshirish uchun

import telebot  # Telegram bot yaratish uchun kutubxona
from moviepy import VideoFileClip  # type: ignore #Videoni ochish, audio ajratish uchun

# 2-bosqich > Botni telegramga ulash
TOKEN = (
    "8589379335:AAH4Np7N1sAs20QRAQwP1ElkFBSK5QfYDxo"  # BotFather bergan maxfiy kalit
)
bot = telebot.TeleBot(TOKEN)  # botni Telegram serveriga ulaydi


# 3-bosqich  >  START buyrug'ini ushlash
@bot.message_handler(
    commands=["start"]
)  # Bu dekorator — botga shuni deydi:  “Foydalanuvchi /start deb yozsa — pastdagi funksiyani ishga tushir.”
def start(message):  # Bu funksiyaga message (telegramdan kelgan xabar) keladi.
    bot.reply_to(
        message, "\n 🎬 Videoni yuboring 3 soniya kuting \n🎙️audioga aylantirib beraman !  \n \n🧏‍♀️  Faqat video yuklang tog'ridan to'g'ri link uchun hali dasturlanmagan ! "
    )  # Bu esa shu xabarga javob qaytaradi.


@bot.message_handler(func=lambda message:True)
def get_fun(message):
    bot.reply_to(message,"Bot to'g'ri ishlashi uchun  /start  buyrug'ini yuboring !")


# 4-QISM: VIDEONI USHLASH HANDLERI
@bot.message_handler(content_types=["video"])
def video_to_audio(message):
    # 5-QISM: VIDEONI TELEGRAM SERVERIDAN YUKLASH
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # 6-QISM: VIDEONI DISKKA YOZIB QO‘YISH
    video_path = "input.mp4"
    audio_path = "output.mp3"

    with open(video_path, "wb") as f:
        f.write(downloaded_file)  # videoni diskka yozadi

    # 7-QISM: VIDEO → AUDIO AJRATISH
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    # 8-QISM: AUDIO FAYLNI FOYDALANUVCHIGA YUBORISH
    with open(audio_path, "rb") as a:
        bot.send_audio(message.chat.id, a)

    # 9-QISM: FAYLLARNI O‘CHIRIB TASHLASH
    video.close()
    os.remove(video_path)
    os.remove(audio_path)


# 10-QISM: BOTNI ISHGA TUSHIRISH
print("Starting the bot  ...")
bot.polling()







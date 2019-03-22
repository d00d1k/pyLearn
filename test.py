import telebot

token = '849320380:AAHkt-L6ACc_m2U6BF0skhgNUjssLJqbtqg'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def Welcome(message):
    bot.reply_to(message, """
Welcome\
""")

@bot.message_handler(content_types=['text'])

def text(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['sticker'])

def sticker(message):
    bot.send_sticker(message.chat.id , message.sticker.file_id)

@bot.message_handler(content_types=['photo'])

def photo(message):
    bot.send_photo(message.chat.id, message.photo[len(message.photo)-1].file_id)

@bot.message_handler(content_types=['video'])

def video(message):
    bot.send_video(message.chat.id, message.video.file_id)

@bot.message_handler(content_types=['audio'])

def audio(message):
    bot.send_audio(message.chat.id, message.audio.file_id)

@bot.message_handler(content_types=['document'])

def document(message):
    bot.send_document(message.chat.id, message.document.file_id)



if __name__ == '__main__':
     bot.polling(none_stop=True)

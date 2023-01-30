import telebot
import openai

# initialize OpenAI API client
openai.api_key = " enter open ai api key here "

bot = telebot.TeleBot(' enter telegram token here ')

@bot.message_handler(commands=['reply'])
def generate_reply(message):
    try:
        if message.chat.type == "private":
            chat_id = message.from_user.id
            bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Use this command in a group and reply to a message.")
            return
        reply_to_message = message.reply_to_message # get the message that the '/reply' command is replying to
        prompt = reply_to_message.text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )
        bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=response["choices"][0]["text"])
    except Exception:
        bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text="Use this command as a reply to a message.")

@bot.message_handler(commands=['gpt'])
def generate_gpt(message):
    if message.chat.type != "private":
        # message was sent in a group, respond to the group
        chat_id = message.chat.id
    else:
        # message was sent in private chat, respond to the sender
        chat_id = message.from_user.id
    prompt_array = message.text.split()[1:]
    if len(prompt_array) < 2:
        bot.send_message(chat_id=chat_id, reply_to_message_id=message.message_id, text="Please provide a message after the command '/gpt'")
        return
    prompt = message.text.split()[1:] # get the text after the command '/gpt'
    prompt = ' '.join(prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048
    )
    bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, text=response["choices"][0]["text"])

bot.polling()

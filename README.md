# Telegram Bot with OpenAI Integration

This Telegram Bot is built with Python and the TeleBot and OpenAI libraries. It allows users to generate responses to messages sent in Telegram groups or private chats using OpenAI's text generation API.

## Demo 
[@GPTReplyBot](https://t.me/GPTReplyBot)

## Tools Used
1. [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) - A Python wrapper for the Telegram Bot API
2. [OpenAI API](https://beta.openai.com/docs/api-reference) - OpenAI's language generation API

## Deployment
1. Clone the repository to your local machine: 
$`git clone https://github.com/dhir4j/chatgpt-bot-telegram.git`

2. Install the required packages: 
$`pip install -r requirements.txt`

3. Replace the [OpenAI API key](https://beta.openai.com/account/api-keys) and [Telegram Bot Token](https://telegram.me/BotFather) in the code with your own.

4. Run the program: 
$`python main.py`

## Usage
1. `/reply` - generates a text response as a reply to a message in a group.
2. `/gpt` - generates a text response to a message sent in a private chat.
3. `/gpta` - same like gpt but returns audio
4. `/roasthim` - Use it to roast, to a reply message
5. `/tl` - Translate to English

## To-Do

- [ ] Add /rdan (reply dan)
- [ ] Add /rkaren (reply karen)
- [ ] Optimize reply (check for telegram commands in prompt, if found remove it from array)

## Dev: [@dhir4j](https://t.me/dhir4j)
Postivite for more contributions
## License

[MIT](https://choosealicense.com/licenses/mit/)

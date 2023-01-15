import telebot
import random



bot = telebot.TeleBot("5988404536:AAGql__8HGgs5hFufEuCzyOZj5Pkml0yk_8")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the stone-Paper-Scissors bot! Send /play to start a game.")


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Send /play followed by stone, paper, or scissors to play a game.")


@bot.message_handler(commands=['play'])
def play_game(message):
    choices = ['stone', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    user_choice = message.text[6:].strip().casefold()
    if user_choice in choices:
        bot.reply_to(message, f"I chose {bot_choice}. You chose {user_choice}.")
        if user_choice == bot_choice:
            bot.reply_to(message, "It's a tie!")
        elif (user_choice == 'stone' and bot_choice == 'scissors') or (user_choice == 'paper' and bot_choice == 'stone') or (user_choice == 'scissors' and bot_choice == 'paper'):
            bot.reply_to(message, "You win!")
        else:
            bot.reply_to(message, "I win!")
    else:
        bot.reply_to(message, "Invalid choice. Please send /play followed by stone, paper, or scissors.You entered: " + user_choice)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Please send /play followed by stone, paper, or scissors.You entered:"+message.text)


bot.polling()



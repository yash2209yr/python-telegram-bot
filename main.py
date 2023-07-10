from pip import main
from telegram.ext import *
import keys

print('Starting up bot...')

def start_command(update, context):
    update.message.reply_text(' Hello There!\n Starting the bot....⏳')
    
def help_command(update, context):
    update.message.reply_text(' Happy to help! The list of commands are: \n 👉/start \n 👉/help \n 👉/custom  ')

def custum_command(update, context):
    update.message.reply_text(' This is a custom command! The list of custom words are: \n 👉hello \n 👉how are you \n 👉icloud \n 👉lms \n 👉youtube \n 👉thanks ')
    
 
def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hey there!'
    
    if 'thanks' in text:
        return 'My Pleasure!'
    
    if 'lms' in text:
        return ' https://lms.galgotiasuniversity.edu.in/my/ '
    
    if 'icloud' in text:
        return ' https://gu.icloudems.com/corecampus/student/student_index.php '
    
    if 'how are you' in text:
        return 'I am fine! thanks for asking!'
    
    if 'youtube' in text:
        return ' https://www.youtube.com/ '
    
    return 'Invalid command!'


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''
    
    print(f'user ({update.message.chat.id}) says: "{text}" in: {message_type}')
    
    
    if message_type == 'group':
        if '@mamodokingbot' in text:
            new_text = text.replace('@(mamodokingbot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)
        
    update.message.reply_text(response)
    
    
def error(update, context):
   print(f'update {update} caused error: {context.error}')
   
   
if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher
    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custum_command))
       
    # Messages
    dp.add_handler (MessageHandler(Filters.text, handle_message))
    
    #Errors
    dp.add_error_handler(error)
    
    # Run Bot 
    updater.start_polling(1.0)
    updater.idle()

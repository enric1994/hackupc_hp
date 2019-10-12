import os
import time

from secret import TOKEN as TOKEN

import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

DONE, SUCCESS = range(2)

def start(update, context):

    user = update.message.from_user
    logger.info("User: %s", user.first_name)
    update.message.reply_text(
        'What do you want to print? Send an audio!')

    return 'Audio'



def audio(update, context):

    print('Getting audio...')
    user = update.message.from_user
    audio_file = update.message.voice.get_file()
    name = 'audio.ogg'
    filename = name
    print('Saving audio as "{}"...'.format(filename))
    audio_file.download(filename)
    update.message.reply_text('Generating 3D...')

    return DONE


def success(update, context):
    
    print('Success...')
    user_data = context.user_data

    update.message.reply_text("Done!")

    return ConversationHandler.END


def done(update, context):
    
    print('Done...')
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text("Bye!")

    user_data.clear()
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states={

            'Audio': [ 
                MessageHandler(Filters.voice, audio)
            ],

            SUCCESS: [ 
                MessageHandler(Filters.text, success) 
            ],

            'Done': [ 
                MessageHandler(Filters.text, done) 
            ],

        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    print('Starting demo...')
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

#potrace -s out.ppm
#convert test.png out.ppm 
#ffmpeg -i audio.ogg out.wav

#start telegram and listen
#save OGG
#transform to wav
#return translation to telegram
#crawl shape and texture
#select best shape and texture
#transform shape PNG to PPM
#transform  PPM to SVG
# blender!



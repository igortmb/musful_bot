from Objects.bot import Bot
from locals import BOT_TOKEN
from Objects.response import Response

token = BOT_TOKEN
bot = Bot()

while True:
    try:
        las_updates = bot.get_updates(allowed_updates=['message'])
        for u in las_updates:
            resp = Response(u.message)
            print("update_id:" + str(u.update_id) + ',' + str(u.message.id))
            if u.message.is_command:
                print('Yes')
            else:
                print('No')
        print(las_updates)

    except KeyboardInterrupt:
        raise KeyboardInterrupt('You stopped the Bot!')

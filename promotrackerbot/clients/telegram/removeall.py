from promotrackerbot.infra.redis import RedisClient
from promotrackerbot.clients.steam import extract_appid
from promotrackerbot.clients.telegram.tracklist import tracklist


def removeall(update, context):
    redis = RedisClient()
    redis.connect()

    chat_id = update.effective_chat.id

    user_tracklist = redis.get(chat_id)

    redis.set(chat_id, {})

    answer = "Your list was removed."
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

    redis.close()
    tracklist(update, context)
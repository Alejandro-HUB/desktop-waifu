def fix_stops(message):
    message = str(message)

    while ".." in message:
        message.replace("..", ",")

    return message.replace(")", ".").replace("!", ",")
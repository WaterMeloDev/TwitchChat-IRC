import irc.bot
import irc.strings
import random

class TwitchBot(irc.bot.SingleServerIRCBot):
    COLORS = ['Red', 'Blue', 'Green', 'Purple', 'Orange', 'Teal', 'Pink']

    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        server = 'irc.chat.twitch.tv'
        port = 6667
        super().__init__([(server, port, f'oauth:{token}')], username, username)

    def on_welcome(self, connection, event):
        connection.join(self.channel)
        print("Bot is now connected and running!")

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        username = irc.client.NickMask(event.source).nick
        color = random.choice(self.COLORS)
        colored_username = f'\033[1;{self.COLORS.index(color) + 31}m{username}\033[1;m'
        print(f'{colored_username}: {message}')

if __name__ == '__main__':
    username = 'your_bot_username'
    client_id = 'your_client_id'
    token = 'your_oauth_token'
    channel = 'target_channel_name'
    
    bot = TwitchBot(username, client_id, token, channel)
    bot.start()
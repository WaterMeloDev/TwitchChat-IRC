# Twitch IRC Bot

This is a simple Python script that creates a Twitch IRC bot using the irc library.
The bot connects to a specified Twitch channel's chat room and displays messages
from users along with randomly colored usernames.

## Requirements

- Python 3.x installed on your machine.
- A valid Twitch account.
- Obtain the following information from your Twitch account:
  - `username`: Your bot's Twitch username.
  - `client_id`: Your Twitch application's client ID.
  - `token`: OAuth token for the bot's authentication. You can generate one using the [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/).
  - `channel`: The Twitch channel name (without the "#" symbol) where the bot will join.

## Usage

1. Clone or download this repository to your local machine.
2. Open the terminal/command prompt and navigate to the project directory.

3. Install the required dependencies using the following command:

```sh
pip install -r requirements.txt
```

4. Open the `chat.py` file and replace the following placeholders with your actual Twitch information:

```python
username = 'your_bot_username'
client_id = 'your_client_id'
token = 'your_oauth_token'
channel = 'target_channel_name'
```

5. Save the changes to the bot.py file.
6. Run the bot script by executing the following command in the terminal:

`python chat.py` or `python3 chat.py`

7. The bot will connect to the specified Twitch channel's chat room, display messages along with randomly colored usernames, and output them to the console.
8. To stop the bot, press `Ctrl+C` in the terminal.


## Notes

- Make sure your Twitch account and bot adhere to Twitch's [Terms of Service](https://www.twitch.tv/p/en/legal/terms-of-service/).
- Be cautious with your bot's OAuth token; do not share it publicly or hardcode it into public repositories.

## Acknowledgments

- This script utilizes the irc library for Python.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/WaterMeloDev/TwitchChat-IRC/blob/main/LICENSE) file for details.


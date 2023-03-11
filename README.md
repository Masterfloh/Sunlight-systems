# Sunlight Systems

Sunlight Systems is an open-source Discord bot project created by masterfloh#7422 and Nic2#2064. It features useful admin commands such as ban, kick, and timeout, among others. For a full list of supported commands, see below!

## Usage

Since this is an open-source project, you are free to copy, use, modify, and distribute the code as you wish. Simply download the repository and replace the bot token in `main.py`.

### Getting a Bot Token

To obtain a Discord bot token, go to the Discord Developer Dashboard [here](https://discord.com/developers/applications), create an application, add a bot to the application, and then get the Discord Bot token. If you need help, please do not hesitate to contact us (contact information can be found on [Masterfloh's profile](https://github.com/Masterfloh)).

## Contributing

- Feel free to support this project by **starring this repository!**
- Contributions are welcome! Please read the [CONTRIBUTING.md](https://github.com/masterfloh/Sunlight-systems/blob/main/CONTRIBUTING.md) before submitting a pull request.

## Commands

- **!ping** - Displays the bot's ping.
- **!poll** - Creates a poll with the specified options.
- **!mute** - Mutes the specified user.
- **!unmute** - Unmutes the specified user.
- **!kick** - Kicks the specified user.
- **!ban** - Bans the specified user.
- **!purge** - Clears the specified number of messages.
- **!warn** - Warns the specified user.
- **!getwarn** - Gets warns from the specified user.
- **!lockdown** - Locks down a channel.
- **!tempban** - Temporarily bans the specified user.
- **!tempmute** - Temporarily mutes the specified user.
- **!unban** - Unbans the specified user.
- **!say** - Repeats your sentence in a cleaner way.
- **!announce** - Announces something to a channel.

## Automatic Moderation

This bot uses the `on_message` event to trigger actions when a message is sent in any channel on the entire Discord. If the message contains any of the words in the `banned_words` list, the message is deleted, and the user is sent a warning message via DM. When editing the banned words list, take note that it is case and spelling sensitive!

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/masterfloh/Sunlight-systems/blob/main/LICENSE.md) file for details.

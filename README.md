# What is Sunlight Systems?

Sunlight Systems is a Open-source discord bot Project made byy masterfloh#7422 and Nic2#2064.
There are tons of usefull features for Admins like Ban, Kick and Timeout features. For a full, updates list of supported commands see below!

# How do I use Sunlight Systems?

Since this is an Open-source project, feel free to copy our code and use, change, and distribute at your own will. Simply download the Repo and change out your Bot token in the main.py

### How do I get this Bot Token?

Simply go to the Discord Developer Dashboard <a href="https://discord.com/developers/applications">here<a>, create a application, add a bot to the application, and then get the Discord Bot token. If you need help, dont hesitate to contact us (Contact infos can be found on <a href="https://github.com/Masterfloh">Masterfloh's Profile<a>
  
 # Contributing

- ### Feel free to support this project by starring this repo!
- Contributions are welcome! Read the [CONTRIBUTING.md](https://github.com/masterfloh/Sunlight-systems/blob/main/CONTRIBUTING.md) before submitting a pull request!


# Commands

- **!ping**  Displays the bot's ping
- **!poll** Creates a poll with the specified options
- **!mute** Mutes the specified user
- **!unmute** Unmutes the specified user
- **!kick** Kicks the specified user
- **!ban** Bans the specified user
- **!purge** Clears the specified number of messages
- **!warn** Warns the specified user
- **!getwarn** Gets warns from the specified user
- **!lockdown** Locks down a channel
- **!tempban** Tempbans a specified user
- **!tempmute** Tempmute a specified user
- **!unban** Unbans the specified user
- **!say** Repeats your sentence in a cleaner way
- **!announce** Announces something to a channel
  
 # Automatic Moderation
  
This bot uses the on_message event to trigger actions when a message is sent in any channel on the entire Discord. If the message contains any of the words in the banned_words list, the message is deleted and the user is sent a warning message via dm. When editing the banned words list, take note of the fact that it is case and spelling sensitive!

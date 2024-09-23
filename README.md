# :keyboard: Spill the beans

Spill the beans is a **Discord bot** that allows users to send private messages to a dedicated channel in your server.
The twist is that you can select the probability of a message being sent anonymously. 


## 🚀 Features

- **Private Message Relay**: Users can send private messages to the bot, and these messages are forwarded to a designated discord server channel.
- **Anonymous Mode**: You can set the proabibility to reveal the senter's name to 0, so all messages will be anonymous.
- You can choose among **two languages**. English and Greek. 
- **Configurable Probability**: Set the likelihood of messages being sent anonymously using a probability setting.

## ⚙️ Bot Configuration

To configre the bot for your own server you should change the variable values in the file **Settings.py**.

1. Add a variable with the name "token" 
*e.g. token = 'token_code'*

2. Add the channelID that the bot will forward the messages. 
*e.g. channelID = 1234567891012345678*

3. Configure the probability to reveal the senter of a message
*e.g. probability = 25 means that there is a probability of 1/4 to reveal the senter of the message*

4. Configure the cooldown time until the same person can sent a message.
*e.g. cooldown = 60*

5. Choose the language ('en' for English and 'gr' for Greek) 
lang = 'en'

## 🔧 Commands

- There are no commands.

## 🤖 Usage

1. Invite the bot to your Discord server.
2. Set up the relay channel where the bot will post messages.
3. Users can send a direct message to the bot.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.

## 📧 Contact

For any questions or support, feel free to reach out on GitHub or contact me directly.

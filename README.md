# DiscordBot
Made using [discord.py](https://pypi.org/project/discord.py/) API. Still in development, Hosted on my Raspberry Pi 4.

# Functions
* `>covid` : COVID-19 update in India! Data from CovIndia.com
* `>covidState` : COVID-19 update state-by-state
* `>start` - To check if the bot is still awake
* `>help`  - To check what all the bot can do
* `>weatherUpdate cityName ` - Gives the current weather in the city u input
* `>intNews` - Gives global news
* `>indNews` - Gives Indian news
* `>members` - Get members of current server
* `>admins`  - Get admins of current server
* `>owner`   - Get the owner of the bot
* `>kick @mention reason` - Kick the mentioned member
* `>ban  @mention reason` - Ban the mentioned user
* `>mute @mention` : Mute the mentioned user
* `>logout`  - The bot logs out
* `>invisible` : The Bot goes invisible
* `>visible` : The Bot comes back visible

Notifies user leaving server. Can recognise its owner.

Wishes good night, and replies back when you initiate chat like "Hey" or "Hi"

Also has some small Easter eggs (try sending ok boomer) 😉

Note : `You need to have the required permissions in the channel for kick or ban to work`

# APIs
Below are the list of APIs used in the discord bot:
* [discord.py](https://pypi.org/project/discord.py/) - The main API for the bot
* [News API](https://newsapi.org/) - API for latest news
* [OpenWeather](https://openweathermap.org/api) - API for latest weather
* [CovIndia](https://covindia.com) - API for COVID-19 data
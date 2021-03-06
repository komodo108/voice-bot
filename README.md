# Quick Bot
A Quick Discord bot in Python for the [AstroSoc](http://astrosoc.club/) discord

### Features
- A way to show cool space images from Google
- Automute people joining a channel
- Give a role to people in voice

### TODO
- [ ] Allow users to select to follow movie night notifications
- [ ] Automate movie night notifications
- [ ] Simple server moderation, e.g. give people role upon join

### Cloning
Ensure you create a `config/tokens.json` file, holding the following keys:
- `discord`: A Discord Bot Token
- `google_api`: An API Key for Google Custom Search
- `google_cx`: A key to a [Google Custom Search Engine](https://cse.google.com/cse)

You should also ensure you create a `config/usage.json` file to hold the usage of limited APIs.
Currently, this file holds the following keys:
- `google`: The number of calls to the Google API

We use `pipenv` for package management, ensure this is installed with `pip install pipenv`.
Update the packages with `pipenv update`, finally run with `pipenv run python source/main.py`.

### Discord Setup
To run this bot on a Discord server, the server must have the following roles:
- `InVoice`: A role indicating whether someone is currently in voice
- `VC Overwrite`: A role allowing users to overwrite the automute
- `Crew`: Moderator role

The following voice channels should also be present:
- `Moive Night`: A channel where people should be quiet
- `AFK`: AFK Channel
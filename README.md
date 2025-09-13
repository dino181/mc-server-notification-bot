# Minecraft server status notifier

A discord bot that notifies the status of a minecraft server.

## Pre-requisites
- Docker
- A discord bot token

## Run 
### Env file
First add a .env file with the following content: 
```
TOKEN=<your-token-here>
```
### Docker
Use the run script (`./run.sh`) to start a detached docker with the bot. 

### Manual
Create a venv with the `venv.sh` script and install the requirements.
Then simply run `python3 main.py` and the bot should start.

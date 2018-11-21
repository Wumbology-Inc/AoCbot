# AoCbot

A small Discord bot for the yearly [Advent of Code](https://adventofcode.com) event!

Head over to the [Python Discord](https://discord.gg/3Abzge7) to see it in action!

Built with [Discord.py](https://github.com/Rapptz/discord.py)

## What is Advent of Code?
Advent of Code (AoC) is an series of small programming puzzles for a variety of skill levels, run every year during the month of December.

They are self-contained and are just as appropriate for an expert who wants to stay sharp as they are for a beginner who is just learning to code. Each puzzle calls upon different skills and has two parts that build on a theme.

## What is AoCbot?
AoCbot provides a set of helper commands for users participating in the event. The bot may be used in its entirety, or the functionality can be inserted into an existing bot framework.

## Installation
With Python 3.7 or newer installed, clone (or download) the repository from GitHub:

```
$ git clone https://github.com/sco1/AoCbot.git
```

Install and activate a virtual environment for the bot to run in. This is optional but highly encouraged:

```
$ python3 -m venv ./.venv
$ source ./.venv/bin/activate
```

Install project requirements:

```
$ pip install -r requirements.txt
```

### Configuration
There are 3 configurations that need to be set for proper functionality of the bot

#### Environment variables
The bot relies on two environment variables being set:

##### `AOCBOT_TOKEN`
Your bot's authentication token. This is obtained from Discord's developer portal.

##### `AOC_SESSION_COOKIE`
Your Advent of Code session cookie, used to authenticate to the private leaderboard API. This can be obtained using your browser's developer console after you've authenticated to AoC. Session cookies typically last for a month.

#### Bot constants
The constants used by the bot are stored in `./bot/constants.py`

```python
class AdventOfCode:
    leaderboard_cache_age_threshold_seconds = <int>
    leaderboard_id = <int>
    leaderboard_join_code = <str>
    leaderboard_max_displayed_members = <int>
    session_cookie = os.environ.get("AOC_SESSION_COOKIE")
    year = <int>
```

#### About AoC Embed
Your private leaderboard details need to be inserted into the `"Join our private leaderboard!"` field of the JSON file, located in `./bot/resources/advent_of_code/about.json`

## Running the bot
After installing on the desired host, the bot can be run using:

```
$ python3 -m bot
```

## Command reference
### `about`
Displays an embed with general information about the event

This command utilizes Discord's embed fields to delimit the information. Fields are specified in `./bot/resources/advent_of_code.json`

### `join`
Provides a link & code to join the your private AoC leaderboard

Your credentials can be specified in your configuration file.

### `leaderboard`
Display an embed with your current private leaderboard stats

NOTE: To reduce load on the AoC API, this information is cached. The cache is checked only when the leaderboard command is invoked and updated if it's older than the configured threshold.
from os import environ


class Emojis:
    star = "\u2B50"
    christmas_tree = u"\U0001F384"


class AdventOfCode:
    leaderboard_cache_age_threshold_seconds = 3600
    leaderboard_id = None
    leaderboard_join_code = None
    leaderboard_max_displayed_members = 10
    session_cookie = environ.get("AOC_SESSION_COOKIE")
    year = 2019

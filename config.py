import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6248129136"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("hina × assistant")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-b567e50c-47a5-41c8-a6d5-9d38fd456c2c")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sinu_bots")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/botkilda")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/3c3ab79fba0fa91a4ae8e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/c603be89cbd04d9d49ebd.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/b838a5d402196d30068ce.jpg"
STATS_IMG_URL = "https://telegra.ph/file/3c3ab79fba0fa91a4ae8e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8d050586cd6693e8f2ee6.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8d050586cd6693e8f2ee6.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/bd24003547eb253e2bb9a.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b838a5d402196d30068ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/b838a5d402196d30068ce.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/c71f53a6d7ac49f57e9b8.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/c71f53a6d7ac49f57e9b8.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/c71f53a6d7ac49f57e9b8.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:"https://t.me/+2jTdwR9j7XE3MDc1"
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):"https://t.me/+kIfyCKWO82AxODk9"
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):"https://t.me/+2jTdwR9j7XE3MDc1"
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters
from database import get_db_general_rtb
from utils import get_restarted

super_sudoers = [1748768168]

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 22645003))
API_HASH = getenv("API_HASH", "1ad9ff9e341f37e5c2aebc34527ae9f2")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://lucifer:ASShaw96@lucifer.vuows.mongodb.net/lucifer?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 20000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1748768168))
OWNER = int(getenv("OWNER"))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/qwert200/bote",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ah07v")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ah07v")
channel = getenv("channel", "")


# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


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

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
disabled_plugins = []
get_bot_information = []
sudoers = []
backup_file = []
developer = []
command = ["/"]
chatstats = {}
userstats = {}
clean = {}

autoclean = []


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
STATS_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
STREAM_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/db83c3505d2e7a9276cfe.png"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

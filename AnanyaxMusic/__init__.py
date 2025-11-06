from AnanyaxMusic.core.bot import Ananya
from AnanyaxMusic.core.dir import dirr
from AnanyaxMusic.core.git import git
from AnanyaxMusic.core.userbot import Userbot
from AnanyaxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

akash = Ananya()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID")19514347)
API_HASH = getenv("API_HASH")33cc018322498f40a5fa773f090a1b5e)

BOT_TOKEN = getenv("BOT_TOKEN", 7565048094:AAGUroA1pIrLBZchPP5PIuseR2av6fZs8-Y)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID")6366762649)

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", BAEpw-sACn6QYDWTwmxblsLDx6c5Gt51rdllQRGXy4cCnEhDQnCNKRGQ8kH-nWxqtFzeAin8lcYfg9KwjjhvII1w6OXGuoVdfbH_rjQgezxfAnUObrtkmQydQkuXinpEZlJ71sOqTWY_eJi6JaQ5TfUaq9D1GxrSEy62bzQYsS3EwtmFXm67s_0QATSprzBprr-NHIyJNVK8EF4MH7sCyfzTVzAeYy1sdEzB2UhUncevGL3HX2owozmuAWxU0N-Q3Q-oyaxa9Sdix5skPwCqyA4uUDuwiw4V6MoQVujcOrWQ6EvgQZCHUOibd1AlYSkTz-Cmo1WqTboJgXoZC6oP03pC7UQV3QAAAAHZ6ojDAA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/bottdestekk")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/bottdestekk")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6366762649").split()))


FAILED = "https://telegra.ph/file/dfa517fd00b6ca5f7ac9.jpg"

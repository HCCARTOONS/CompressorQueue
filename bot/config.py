#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = 8222280
    API_HASH = b8f7e769581a8d04b49d96ed75b612b0
    BOT_TOKEN = 5345450523:AAHD-x6l51k37-0cgCRQpBVvye31nqKMWOQ
    DEV = 1872074304
    OWNER = 2119981197
    OWNER_CHAT = -1001679268215
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/75ee20ec8d8c8bba84f02.jpg"
    )
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()

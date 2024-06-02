#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "8440502"
    API_HASH = "e77474ae3075f4000d3418c5a5a3a112"
    BOT_TOKEN = "5785661511:AAHDvS081-T8ZJYjhf9tX7KIXXA2IwyZn4E"
    DEV = "2043144248"
    OWNER = "5623055023"
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Op-Leech/Mirror' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = "https://graph.org/file/b06a165dd7b8b064ea549.jpg"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)

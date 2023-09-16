#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "5441410"
    API_HASH = "a1a4fe7d23328f419d98a58339fd9980"
    BOT_TOKEN = "5568498977:AAFLmxBr-b4EASZ9JTTLVlrslDVis0zOZ3U"
    DEV = "2023056811 , 5215459301"
    OWNER = "2023056811"
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = "https://telegra.ph/file/c63c3bcf7512f14750c9e.jpg"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)

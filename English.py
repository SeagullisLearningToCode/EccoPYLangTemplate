from datetime import *
td = datetime.now()

# Strings --> Ingame and HUD
yt_friendly = "Nothing"
hp_txt = "Health"
air_txt = "O2"
tit_bttm_txt = "PC Remake Concept"
if yt_friendly is False:
    wtrmark_txt = "SIS Programming (2021)" # Insert fake company name here
elif yt_friendly == "Nothing":
    wtrmark_txt = f"/--_ BETA: {td}"
else:
    wtrmark_txt = "Coded by: SeagullInSeagulls /--_"
# Warning Screen
hu_ws_str1 = "WARNING"
hu_ws_str2 = "Even if it's illegal or not, it's harmful to feed or attempt to feed and even harass Wildlife"
hu_ws_str3 = "Not only it's harmful but you are wasting food..."

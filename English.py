from datetime import *
# Today's Date
td = date.today() # More simple than "datetime.now()"
td_c_s = str(td) # Converts the current date into a String
td_c_s_yo = td_c_s[0:4] # Get year only
# Today's Time
tt = datetime.now()

# Strings --> Ingame and HUD
yt_friendly = "Nothing"
hp_txt = "Health"
air_txt = "O2"
tit_bttm_txt = "PC Remake Concept"
if yt_friendly is False:
    wtrmark_txt = f"SIS Programming ({td_c_s_yo})" # Insert fake company name here
elif yt_friendly == "Nothing":
    wtrmark_txt = f"/--_ BETA: {td}"
else:
    wtrmark_txt = "Coded by: SeagullInSeagulls /--_"
# Warning Screen
e_ws_str1 = "WARNING"
e_ws_str2 = "Even if it's illegal or not, it's harmful to feed or attempt to feed and even harass Wildlife"
e_ws_str3 = "Not only it's harmful but you are creating unhealthy diets for the wildlife."
e_ws_str4 = f"DATE: {td.strftime('%Y.%m.%d')}"
e_ws_str5 = f"{tt.strftime('%p %I:%M')}"

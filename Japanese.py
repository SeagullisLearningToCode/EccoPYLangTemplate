# Japanese (Google Translated)
# 今日の日付
from datetime import *
td = date.today() # 「datetime.now（）」よりも単純です
td_c_s = str(td) # 現在の日付を文字列に変換します
td_c_s_yo = td_c_s[0:4] # 年のみ取得
# 今日の時間
tt = datetime.now()

# Strings
yt_friendly = "何もない"
hp_txt = "健康"
air_txt = "O2"
tit_bttm_txt = "PCリメイクのコンセプト"
if yt_friendly is False:
    wtrmark_txt = "SIS Programming (2021)"
elif yt_friendly == "何もない":
    wtrmark_txt = f"/--_ ベータ: {td}"
else:
    wtrmark_txt = "コード化：SeagullInSeagulls / --_"

e_ws_str1 = "警告"
e_ws_str2 = "違法であろうとなかろうと、餌を与えたり、餌を与えようとしたり、野生生物に嫌がらせをしたりすることは有害です。"
e_ws_str3 = "それは有害であるだけでなく、あなたは彼らのために作られていない食べ物に頼るように彼らの食事を変えています"
e_ws_str4 = f"DATE: {td.strftime('%Y.%m.%d')}"
e_ws_str5 = f"{tt.strftime('%p %I:%M')}"

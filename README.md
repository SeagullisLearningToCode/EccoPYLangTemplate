# EccoPYLangTemplate
This is a template for those who want to localize EccoPY in a different Langauge. (Expect this to be updated)

The code in EccoPY has already been translated in...
- English
- German
- Japanese
- Hungarian

When EccoPY gets released the folder to store these are in...

**dataE\dataTXT\Labels\Lang\<Insert Langauge Name Here>\<Insert Name Here>.py**

# Restrictions
Yes, there are restrictions to this due to how Pygame works
You can't...
- use the new line operation "\n"
- more will be listed here, I hadn't used this alot, this list will be updated when I find a new limitation.

If you don't know how text input works in Pygame, then click the links below
- [https://www.pygame.org/docs/ref/font.html] (Font)
- [https://www.pygame.org/docs/ref/freetype.html] (FreeType)


# Documentation
In-Game Strings
- yt_friendly = Is just to change the string for the Watermark
- hp_txt = Is the Health bar text which is located inside the health bar (of course)
- air_txt = Is the same thing as hp_txt but deals the air text (really no reason to edit this since its using the molecule name O^2)
- tit_bttm_txt = Title Below the ECCO logo
- wtrmark_txt = Is placed the bottom-right as a watermark

Warning Screen Strings
- e_ws_str1 = Placed at Center Top
- e_ws_str2 = Placed at the near middle
- e_ws_str3 = Placed at below str2 as if it was a new line

Note that in Japanese.py, it's the same thing as English.py except that str3 in Warning Screen Strings is slightly longer than English.py.

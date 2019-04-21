import os
from PIL import Image
import sys
sys.path.append('/path/to/dir')

import pyocr
import pyocr.builders

import pyautogui

tools = pyocr.get_available_tools()

if len(tools) == 0:
	print("NO OCR tool found")
	sys.exit(1)

tool = tools[0]
#print("Will use tool '%s'" % (tool.get_name()))
langs = tool.get_available_languages()
#print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
#print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.


for i in range(40):

	s = pyautogui.screenshot(region=(500, 800, 600, 300))
	s.save("test.png")
	
	txt = tool.image_to_string(
	 Image.open("test.png"),
	 lang=lang,
	 builder=pyocr.builders.TextBuilder()
	)
	# txt is a Python string
	
	print(txt)
	
	cmd = "osascript -e 'tell application \"System Events\" to keystroke \"" + txt + "\"'"         
	os.system(cmd)

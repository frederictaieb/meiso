import os
import pyttsx3
from google_trans_new import google_translator  

dir_name = "data"
ext_file = ".txt"

src_name = input ("Enter file to read : ")
if "".__eq__(src_name):
	src_name = "livre"
src_path = os.path.join(dir_name, src_name + ext_file)

f_src = open(src_path, "r")

translator = google_translator()  

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[38].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)

for line in f_src:
	if not line.isspace(): 
		translate_text = translator.translate(line, lang_src='en', lang_tgt='fr')
		engine.runAndWait(translate_text)


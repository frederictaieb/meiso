import os
from google_trans_new import google_translator  
#translator = google_translator()  
#translate_text = translator.translate('Hola todo el mundo!', lang_src='es', lang_tgt='fr')  
#print(translate_text)

#f_src = open("src.txt", "r")
#f_dst = open("dst.txt", "a")

dir_name = "data"
ext_file = ".txt"

src_name = input ("Enter source filename (src) : ")
if "".__eq__(src_name):
	src_name = "src"
src_path = os.path.join(dir_name, src_name + ext_file)

dst_name = input ("Enter destination filename (dst) : ")
if "".__eq__(dst_name):
	dst_name = "dst"
dst_path = os.path.join(dir_name, dst_name + ext_file)

f_src = open(src_path, "r")
f_dst = open(dst_path, "w")


#translator = google_translator()  
#translate_text = translator.translate(f_src.read(), lang_src='en', lang_tgt='fr') 

#f_dst.write(translate_text)
#f_dst.close()

translator = google_translator()  
i = 0
#with open(src_path) as fp:
for line in f_src:
	if not line.isspace(): 
		translate_text = translator.translate(line, lang_src='en', lang_tgt='fr')
		f_dst.write(translate_text)
		f_dst.write("\n")

f_dst.close()

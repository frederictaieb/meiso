import sys
import os
import time
from google_trans_new import google_translator 

class Translator : 
	def __init__(self, kooby, lang_src="en", lang_tgt="fr"):
		self.kooby = kooby
		self.lang_src = lang_src
		self.lang_tgt = lang_tgt

		# get lines from text file
		f_in  = open(self.kooby.get_path("txt"), "r")
		self.lines = lines = f_in.readlines()
		f_in.close()

		#transform lines in paragraphs
		self.paragraphs=[]
		#print(self.lines[0])
		self.lines_to_paragraph()
		self.translate()

	def clean(self):
		return

	def lines_to_paragraph(self):
		i = 0
		paragraph = ""

		l = self.lines[i]

		while (True):
			while(l!='\n'):
				paragraph = paragraph + l
				i = i+1
				if i >= len(self.lines):
					break
				l = self.lines[i]

			if len(paragraph) > 1 :
				paragraph = paragraph.replace("\n", " ")
				paragraph = paragraph + "\n"
				self.paragraphs.append(paragraph)
			i=i+1

			if i >= len(self.lines):
				break
			else:
				paragraph = ""
				l = self.lines[i]
			
	def __str__(self):
		return (str(self.paragraphs))
			

	def translate(self):
		translator = google_translator()

		f = open(self.kooby.get_path('txt') + "-fr", 'w')

		for line in self.paragraphs:
			translated_text = translator.translate(line, lang_src=self.lang_src, lang_tgt=self.lang_tgt)
			f.write(translated_text)
			f.write("\n\n")

		f.close()
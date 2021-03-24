import sys
import os
import time
import pyttsx3
import html2text
from epub_conversion.utils import open_book, convert_epub_to_lines
from google_trans_new import google_translator  

class convertor : 
	def __init__(self, filename):
		f = open(filename)
		f.close()
		self.book = open_book(filename)
		self.lines = convert_epub_to_lines(self.book)

	def to_html(self):
		output = open("output.html", "a")
		for l in self.lines:
			output.write(l)
		output.close()

	def to_txt(self):
		output = open("output.txt", "a")
		for l in self.lines:
			output.write(html2text.html2text(l))
		output.close()

class translator : 
	def __init__(self, filename, lang_src="en", lang_tgt="fr"):
		self.filename = filename
		self.lang_src = lang_src
		self.lang_tgt = lang_tgt
		
		#translator
		self.google = google_translator()
		
		#Reader
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('rate', 170)
		if self.lang_tgt == "fr": 
			self.engine.setProperty("voice", self.voices[38].id)
		else : 
			self.engine.setProperty("voice", self.voices[0].id)
		
		# get lines from text file
		f_in  = open(self.filename, "r")
		self.lines = lines = f_in.readlines()
		f_in.close()

		# transform lines in paragraphs
		self.paragraphs=[]
		self.lines_to_paragraph()

	def play(self, paragraph):
		#translated_text = translator.translate(paragraph, lang_src=self.lang_src, lang_tgt=self.lang_tgt)
		#translated_text = self.google.translate(paragraph, self.lang_src, self.lang_tgt)
		translated_text = self.google.translate(paragraph, "en", "fr")
		print (translated_text)
		#self.engine.say(translated_text)
		#self.engine.runAndWait()


	def lines_to_paragraph(self):
		i = 0
		paragraph = ""

		l = self.lines[i]

		while (True):
			while(l!='\n'):
				paragraph = paragraph + l
				i = i+1
				l = self.lines[i]
			paragraph = paragraph.replace("\n", " ")
			paragraph = paragraph + '\n'
			print(paragraph)
			self.play(paragraph)
			self.paragraphs.append(paragraph)

			i=i+1

			if i >= len(self.lines):
				break
			else:
				paragraph = ""
				l = self.lines[i]
			
	def __str__(self):
		return (str(self.paragraphs))
				

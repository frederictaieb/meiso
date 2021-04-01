
from fileable import Fileable
from convertor import Convertor
from translator import Translator
from reader import Reader
import os

class Kooby():

	def __init__(self, folder="data"):
		self.folder = folder
		self.filename = input("Enter EPUB Filename: ")
		self.lang_src = "en"
		self.lang_tgt = "fr"
 
		path_without_ext = os.path.join(self.folder, self.filename ).lower()
		path_with_ext = path_without_ext + ".epub"

		if os.path.exists(path_with_ext):  
			c = Convertor(path_without_ext)
			c.to_txt()
		
			##t = Translator(path_without_ext, self.lang_src, self.lang_tgt)
			#t.google_translate()

			#r = Reader(t.filename, self.lang_tgt)
			#r.play()

		else: 
			print("File {} is Missing".format(path))

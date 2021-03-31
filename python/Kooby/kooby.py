
from fileable import Fileable
from convertor import Convertor
from translator import Translator

class Kooby(Fileable):

	def __init__(self, folder="data", name="book"):
		super().__init__(folder, name)
		
		#Convert epub file in HTML and TXT files
		#c = Convertor(self)
		t = Translator(self)
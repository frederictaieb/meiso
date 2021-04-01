
import html2text
from fileable import Fileable
from epub_conversion.utils import open_book, convert_epub_to_lines

class Convertor() : 
	def __init__(self, filename):
		self.__filename = filename
		self.book = open_book(self.filename + ".epub")
		self.lines = convert_epub_to_lines(self.book)

	@property
	def filename(self):
		return self.__filename
	

	def to_html(self):
		output = open(self.filename + ".html", "w")
		for l in self.lines:
			output.write(l)
		output.close()
		return
#
	def to_txt(self):
		h = html2text.HTML2Text()
		h.ignore_links = True
		h.ignore_images =True
		h.single_line_break = True

		print("Conversion EPUB -> TXT...")
		output = open(self.filename + ".txt", "w")

		for l in self.lines:
			output.write(h.handle(l))
		output.close()
		print("OK")
		return



import html2text
from fileable import Fileable
from epub_conversion.utils import open_book, convert_epub_to_lines

class Convertor() : 
	def __init__(self, kooby):
		#super().__init__(folder, name, ext)
		self.kooby = kooby
		self.book = open_book(self.kooby.get_path())
		self.lines = convert_epub_to_lines(self.book)
		
		self.to_html()
		self.to_txt()

	def to_html(self):
		output = open(self.kooby.get_path("html"), "w")
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

		output = open(self.kooby.get_path("txt"), "w")

		for l in self.lines:
			output.write(h.handle(l))
		output.close()
		return


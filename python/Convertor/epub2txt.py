#!/usr/bin/env python3

import sys
from epub_conversion.utils import open_book, convert_epub_to_lines
import html2text
from tools import *

def convert(name):
	book = open_book(name)
	lines = convert_epub_to_lines(book)
	return lines

def save(lines, format="html"):
	output = open("output." + format, "a")
	if format == "html" :
		for l in lines:
			output.write(l)
	else: 
		for l in lines:
			output.write(html2text.html2text(l))
	output.close()

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
    	try:
    		f = open(arg)
    		f.close()
    		lines = convert(arg)
    		save(lines)
    		save(lines, "txt")
    	except FileNotFoundError:
    		print("File not accessible")

if __name__ == "__main__":
    main()
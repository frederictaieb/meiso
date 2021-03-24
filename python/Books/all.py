#!/usr/bin/env python3

from tools import convertor, translator, reader

def main():



	#c = convertor("sapiens.epub")
	#c.to_html()
	#c.to_txt()

	#r = reader("output.txt")
	#r.play()

	t = translator("output.txt")
	t.translate()
	r = reader("output-fr.txt", "FR")
	r.play()

if __name__ == "__main__":
    main()
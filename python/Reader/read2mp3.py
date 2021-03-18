import os
import pyttsx3

# voice engine initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

# Language choice, Default english
lang = input ("Do you want to read in French (y/N)? ")
if lang.__eq__(""):
	lang = "N"

# What is bookpath
file = input("Enter filename (data/book.txt): ")

# Set up French Language if french has been chosen (Y), else english 
lang = lang.upper()
if lang.__eq__("Y"):
	engine.setProperty("voice", voices[38].id)	
else: 
	engine.setProperty("voice", voices[0].id)

#Opening file
src_path = os.path.join("data/book.txt")
f_src = open(src_path, "r")

i=0

# Play line by line
for line in f_src:
	if not line.isspace(): 
		print(line)
		engine.say(line)
		engine.save_to_file(line , "test" + str(i) + ".mp3")
		i = i + 1
		engine.runAndWait()


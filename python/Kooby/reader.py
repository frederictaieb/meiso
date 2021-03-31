import pyttsx3
#from fileable import Fileable

class Reader():
	def __init__(self, filename, language = "EN"):
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('rate', 170)
		
		if language == "FR": 
			self.engine.setProperty("voice", self.voices[38].id)
		else : 
			self.engine.setProperty("voice", self.voices[0].id)
		self.filename = filename

	def play(self):
		f = open(self.filename, "r")
		for line in f:
			if not line.isspace(): 
				self.engine.say(line)
				self.engine.runAndWait()
		f.close()

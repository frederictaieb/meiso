class Type : 
	def __init__(self, name, desc, desc_fr):
		self.name = name
		self.desc = desc
		self.desc_fr = desc_fr

	def __str__(self):
		return self.name

class Profil : 
	def __init__(self, name, line1, line2, desc, desc_fr):
		self.name = name
		self.line1 = line1
		self.line2 = line2
		self.desc = desc
		self.desc_fr = desc_fr

class Channel : 
	def __init__ (self, channel, name, gate1, gate2, desc, fr_desc):
		self.channel = channel
		self.name = name
		self.gate1 = gate1
		self.gate2 = gate2
		self.desc = desc
		self.fr_desc = fr_desc

class Center : 
	def __init__(self, name, desc_d, desc_u, desc_d_fr, desc_u_fr):
		self.name = name
		self.desc_defined = desc_d
		self.desc_undefined = desc_u		
		self.desc_defined_fr = desc_d_fr
		self.desc_undefined_fr = desc_u_fr

	def __str__(self):
		return self.name

class Gate :
	def __init__(self, num, name, desc, fr_desc, center):
		self.num = num
		self.line = 0
		self.name = name
		self.desc = desc
		self.fr_desc = fr_desc
		self.center = center

	def __str__(self): 
		return str(self.num)+": "+self.name+"\n"+self.fr_desc+"\n"+str(self.center)
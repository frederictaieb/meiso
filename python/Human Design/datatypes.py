class Type : 
	def __init__(self, name, desc, desc_fr):
		self.name = name
		self.desc = desc
		self.desc_fr = desc_fr

	def __str__(self):
		txt = "Name: {} \n Desc: {} \n Desc_fr: {} \n".format(self.name, self.desc, self.desc_fr)
		return txt

class Profil : 
	def __init__(self, lines, line1, line2, desc, desc_fr):
		self.lines = lines
		self.line1 = line1
		self.line2 = line2
		self.desc = desc
		self.desc_fr = desc_fr

	def __str__(self):
		txt = "Lines: {} \n name1: {} \n name2: {} \n Desc: {} \n Desc_fr: {} \n".format(self.lines, self.name1, self.name2, self.desc, self.desc_fr)
		return txt

class Center : 
	def __init__(self, name, desc_d, desc_u, desc_d_fr, desc_u_fr):
		self.name = name
		self.desc_defined = desc_d
		self.desc_undefined = desc_u		
		self.desc_defined_fr = desc_d_fr
		self.desc_undefined_fr = desc_u_fr

	def __str__(self):
		txt = "Name: {} \n Desc_def: {} \n Desc_undef: {} \n Desc_def_fr: {} \n Desc_undef_fr: {} \n".format(self.name, self.desc_defined, self.desc_undefined, self.desc_defined_fr, self.desc_undefined_fr)
		return txt

class Definition: 
	def __init__(self, name, desc, desc_fr):
		self.name = name
		self.desc = desc
		self.desc_fr = desc_fr

	def __str__(self): 
		txt = "Name: {} Desc: {} \n Desc_fr: {} \n".format(self.name, self.desc, self.desc_fr)
		return txt


class Gate :
	def __init__(self, num, name, desc, desc_fr, center):
		self.num = num
		self.name = name
		self.desc = desc
		self.desc_fr = desc_fr
		self.center = center

	def __str__(self): 
		txt = "Num: {}\n Name: {}\n  Desc:{}\n Desc_fr:{}\n Center: {}\n".format(self.num, self.name, self.desc, self.desc_fr, self.center)
		return txt

class Channel : 
	def __init__ (self, channel, name, gate1, gate2, desc, desc_fr):
		self.channel = channel
		self.name = name
		self.gate1 = gate1
		self.gate2 = gate2
		self.desc =desc
		self.desc_fr = desc_fr

	def __str__(self):
		txt = "Channel: {}\n Name: {}\n  Gate1:{}\n Gate2:{}\n Desc: {}\n Desc_fr: {}\n".format(self.channel, self.name, self.gate1, self.gate2, self.desc, self.desc_fr)
		return txt

class Incarnation_cross : 
	def __init__ (self, name, gate11, gate12, gate21, gate22, desc, desc_fr):
		self.name = name
		self.gate11 = gate11
		self.gate12 = gate12
		self.gate21 = gate21
		self.gate22 = gate22
		self.desc = desc
		self.desc_fr = desc_fr

	def __str__(self):
		txt = "Channel: {}\n Name: {}\n  Gate1:{}\n Gate2:{}\n Desc: {}\n Desc_fr: {}\n".format(self.name, self.gate11, self.gate12, self.gate11, self.gate12, self.desc, self.desc_fr)
		return txt

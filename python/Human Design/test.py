import pandas as pd
import json

from datatypes import *
#from gate import Gate
#from channel import Channel

class Human_design : 

	types = []
	profils = []
	centers = []
	definitions = []
	gates = []
	channels = []
	
	incarnation_cross = []


	def __init__(self):
		self.fill_all()

	def fill_types(self):
		print ("Hello")

	def fill_profils(self):
		print ("Hello")

	def fill_centers(self):
		print ("Hello")

	def fill_definitions(self):
		print("Hello")

	def fill_gates(self):
		data = pd.read_excel("data/gates.xlsx")
		for i in range(0, len(data)):
			num = i+1
			name = data.at[i, 'Name']
			center = data.at[i, 'Center']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'FR']
			g = Gate(num, name, center, desc, desc_fr)
			self.gates.append(g)

	def fill_channels(self):
		data = pd.read_excel("data/channels.xlsx")
		for i in range(0, len(data)):
			channel = data.at[i, 'Channel']
			name = data.at[i, 'Name']
			gate1 = data.at[i, 'Gate1']
			gate2 = data.at[i, 'Gate2']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'FR']
			c = Channel(channel, name, self.gates[gate1-1], self.gates[gate2-1], desc, desc_fr)
			self.channels.append(c)

	def fill_incarnation_cross(self):
		print ("Hello")

	def fill_all(self):
		self.fill_types()
		self.fill_profils()
		self.fill_centers()
		self.fill_definitions()
		self.fill_gates()
		self.fill_channels()
		self.fill_incarnation_cross()

hd = Human_design()
print(hd.channels[2].gate2)


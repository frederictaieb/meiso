import pandas as pd
import json

from datatypes import *

class Human_design : 

	types = []
	profils = []
	centers = []
	definitions = []
	gates = []
	channels = []
	
	incarnation_crosses = []


	def __init__(self):
		self.fill_all()

	def fill_types(self):
		data = pd.read_excel("data/types.xlsx")
		for i in range(0, len(data)):
			name = data.at[i, 'Name']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'Description_FR']
			t = Type(name, desc, desc_fr)
			self.types.append(t)

	def fill_profils(self):
		data = pd.read_excel("data/profils.xlsx")
		for i in range(0, len(data)):
			lines = data.at[i, 'Lines']
			name1 = data.at[i, 'Name1']
			name2 = data.at[i, 'Name2']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'Description_FR']
			p = Profil(lines, name1, name2, desc, desc_fr)
			self.profils.append(p)

	def fill_centers(self):
		data = pd.read_excel("data/centers.xlsx")
		for i in range(0, len(data)):
			name = data.at[i, 'Name']
			desc_d = data.at[i, 'Description_def']
			desc_u = data.at[i, 'Description_undef']
			desc_d_fr = data.at[i, 'Description_def_FR']
			desc_u_fr = data.at[i, 'Description_undef_FR']
			c = Center(name, desc_d, desc_u, desc_d_fr, desc_u_fr)
			self.centers.append(c)

	def fill_definitions(self):
		data = pd.read_excel("data/definitions.xlsx")
		for i in range(0, len(data)):
			name = data.at[i, 'Name']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'Description_FR']
			d = Definition(name, desc, desc_fr)
			self.definitions.append(d)

	def fill_gates(self):
		data = pd.read_excel("data/gates.xlsx")
		for i in range(0, len(data)):
			num = i+1
			name = data.at[i, 'Name']
			center = data.at[i, 'Center']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'Description_FR']
			g = Gate(num, name, desc, desc_fr, center)
			self.gates.append(g)

	def fill_channels(self):
		data = pd.read_excel("data/channels.xlsx")
		for i in range(0, len(data)):
			channel = data.at[i, 'Channel']
			name = data.at[i, 'Name']
			gate1 = data.at[i, 'Gate1']
			gate2 = data.at[i, 'Gate2']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'Description_FR']
			c = Channel(channel, name, self.gates[gate1-1], self.gates[gate2-1], desc, desc_fr)
			self.channels.append(c)

	def fill_incarnation_crosses(self):
		data = pd.read_excel("data/incarnation_cross.xlsx")
		for i in range(0, len(data)):
			name = data.at[i, 'Name']
			gate11 = data.at[i, 'Gate11']
			gate12 = data.at[i, 'Gate12']
			gate21 = data.at[i, 'Gate21']
			gate22 = data.at[i, 'Gate22']
			desc = data.at[i, 'Description']
			desc_fr = data.at[i, 'Description_FR']
			ic = Incarnation_cross(name, gate11, gate12, gate21, gate22, desc, desc_fr)
			self.incarnation_crosses.append(ic)

	def fill_all(self):
		print("Fill Human Design Data Structure... ")
		
		print("Step1 : Filling Types", end='')
		self.fill_types()
		print("\t\tOK")
		
		print("Step2 : Filling Profils", end='')
		self.fill_profils()
		print("\t\tOK")

		print("Step3 : Filling Centers", end='')
		self.fill_centers()
		print("\t\tOK")

		print("Step3 : Filling Definitions", end='')
		self.fill_definitions()
		print("\tOK")

		print("Step4 : Filling Gates", end='')
		self.fill_gates()
		print("\t\tOK")

		print("Step5 : Filling Channels", end='')
		self.fill_channels()
		print("\tOK")

		print("Step6 : Filling Incarnation Crosses ... ", end='')
		self.fill_incarnation_crosses()
		print("\tOK")
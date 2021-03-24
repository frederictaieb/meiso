from humandesign import Human_design_data
from datatypes import Meisien
from datatypes import Human_design

#Build Data from xlsx
hdd = Human_design_data()

m = Meisien("TAIEB", "Frederic", "Athis Mons")

#Enter Human Design
hd = Human_design("Generator", "1/4", "G", "Split Definition", "58", "58-18", "Right Angle Of Service")

#Affect Human Design to Meisien
m.human_design = hd

#Export report to Txt or Html

print(m)



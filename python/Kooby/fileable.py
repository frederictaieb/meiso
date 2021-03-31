class Fileable:
	def __init__(self, folder, name):
		self.__folder = folder
		self.__name = name

	@property
	def folder(self):
		return self.__folder

	@folder.setter
	def folder (self, folder):
		self.folder = folder

	@property
	def name(self):
		return self.__name

	@name.setter
	def name (self, name):
		self.name = name


	def get_path(self, ext='epub'):
		return (self.folder + "/" + self.name + "." + ext)


	def __repr__(self):
		return(str(self.__dict__))
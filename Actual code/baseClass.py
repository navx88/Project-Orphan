class character:

	def __init__(self,name):

		self.name = name

		#Attributes correspond the following fashion
		# 1.Introversion	2.Extroversion	3.Feeling		4.thinking
		# 5.Judging			6.Inuition		7.Perception	8.Sensing
		self.attributes = [0,0,0,0,0,0,0,0]

		#Equipment is catalogued in the following fashion
		# 1. Left Arm 	2. Right Arm 	3. Torso
		# 4. Feet		5. Head
		self.equipment = []
		self.currentStatus = 'none'

	def equipItem(self, item):
		self.equipment[item.type] = item

	def assignStatus(self, status):
		self.currentStatus = status
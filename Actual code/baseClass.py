<<<<<<< HEAD
=======
import itemClass.py

>>>>>>> 96ee375355d43976c6828be9e3944e5779cba1df
class character:

	def __init__(self,name):

		self.name = name

		#Attributes correspond the following fashion
<<<<<<< HEAD
		# 1.Introversion	2.Extroversion	3.Feeling		4.thinking
		# 5.Judging			6.Inuition		7.Perception	8.Sensing
		self.attributes = [0,0,0,0,0,0,0,0]

		#Equipment is catalogued in the following fashion
		# 1. Left Arm 	2. Right Arm 	3. Torso
		# 4. Feet		5. Head
		self.equipment = []
		self.currentStatus = 'none'

=======
		# 0.Introversion	1.Extroversion	2.Feeling		3.thinking
		# 4.Judging			5.Inuition		6.Perception	7.Sensing
		self.attributes = [0,0,0,0,0,0,0,0]

		#Equipment is catalogued in the following fashion
		# 0. Left Arm 	1. Right Arm 	2. Torso
		# 3. Feet		4. Head
		self.equipment = []
		self.currentStatus = 'none'

	#Use this function for upgrading equipment, upgrading can be just creating a
	#the upgraded item and equiping it.
>>>>>>> 96ee375355d43976c6828be9e3944e5779cba1df
	def equipItem(self, item):
		self.equipment[item.type] = item

	def assignStatus(self, status):
		self.currentStatus = status
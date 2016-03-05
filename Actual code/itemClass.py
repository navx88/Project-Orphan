
class itemClass(self, name):

	def __init__(self,idNum,name,itemType,description):
		self.idNum = idNum
		self.name = name
		self.itemType = itemType
		self.description = description
		self.stats = [0,0,0,0,0,0,0,0]
		
	def assignStats(self,intr,ext,fee,thi,jud,sen,intu,per):
		self.stats[0] = intr
		self.stats[1] = ext
		self.stats[2] = fee
		self.stats[3] = thi
		self.stats[4] = jud
		self.stats[5] = sen
		self.stats[6] = intu
		self.stats[7] = per

	def displayStats(self, name):

		for element in self.stats:
			if element != 0:
				if element == self.stats[0]:
					print "Introversion " + element

				elif element == self.stats[1]:
					print "Extroversion " + element

				elif element == self.stats[2]:
					print "Feeling " + element

				elif element == self.stats[3]:
					print "Thinking " + element
					
				elif element == self.stats[4]:
					print "Judging " + element

				elif element == self.stats[5]:
					print "Sensing " + element
										
				elif element == self.stats[6]:
					print "Intuition " + element
										
				elif element == self.stats[7]:
					print "Perception " + element

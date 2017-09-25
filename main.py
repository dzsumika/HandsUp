class classroom:
	def __init__(self, className): #Defines the name of the classroom
		self.className = className

	def printList(self): #Prints out the list
		elev = [""]*10
		print "\n"*12
		print "\t\t\t"+self.className.center(27, "#")
		print "\t\t\t"+"#" + elev[0].center(25) + "#"
		print "\t\t\t"+"#" + elev[1].center(25) + "#"
		print "\t\t\t"+"#" + elev[2].center(25) + "#"
		print "\t\t\t"+"#" + elev[3].center(25) + "#"
		print "\t\t\t"+"#" + elev[4].center(25) + "#"
		print "\t\t\t"+"#" + elev[5].center(25) + "#"
		print "\t\t\t"+"#" + elev[6].center(25) + "#"
		print "\t\t\t"+"#" + elev[7].center(25) + "#"
		print "\t\t\t"+"#".center(27, "#")
		print "\n"*5



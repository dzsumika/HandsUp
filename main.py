class classroom:
	def __init__(self, className): #Defines the name of the classroom
		self.className = className

	def printList(self, namn): #Changed the "alg to print out list"
		print "\n"*12
		print "\t\t\t"+self.className.center(27, "#")
		print "\t\t\t#\t\t\t  #"
		for i in range(len(namn)):
			print "\t\t\t"+"#" + namn[i].center(25) + "#"
		print "\t\t\t"+"#".center(27, "#")
		print "\n"*5

tek_cs = classroom("16_tek_cs") #test
arrayList = ["Harry", "Zimon", "Panos", "Nur", "Ahmed"] #listTest... can be changed...
tek_cs.protList(arrayList) #test






import socket, sys, time
class classroom:
	def __init__(self, className): #Defines the name of the classroom
		self.className = className

	def printList(self, namn): #Changed the "alg to print out list"
		print "\n"*12
		print "\t\t\t"+self.className.center(27, "#")
		#print "\t\t\t#\t\t\t  #"
		for i in range(len(namn)):
			print "\t\t\t"+"#" + namn[i].center(25) + "#"
		print "\t\t\t"+"#".center(27, "#")
		print "\n"*5

	def networkHost(self):
		classList = []
		host = "localhost" #primarly
		port = 5000 #Primarly

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((host, port))

		print "Elever kan nu ansluta!"

		while True:
			data, addr = s.recvfrom(1024)
			if data != None:
				classList.append(str(data))
				self.printList(classList)
		s.close()

if __name__ == "__main__":
	klassnamn = raw_input("Vad heter din klass?: ")
	class1 = classroom(klassnamn)
	class1.networkHost()




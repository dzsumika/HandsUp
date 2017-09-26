import socket, sys, time
class elev:
	def __init__(self, namn):
		self.namn = namn

	def sendName(self):
		start = raw_input("")
		if start == "":
			return self.namn
#sdfuhdkm
	def sendHand(self):
		host = "localhost" 
		port = 5001

		server = ("localhost", 5000)

		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				s.bind((host, port))
				#s.sendto("ny", server)
				break
			except:
				port+=1


		while True:
			elevnamn = self.sendName()
			s.sendto(elevnamn, server)
		s.close()

if __name__ == "__main__": 
	name = raw_input("Vad heter du?: ")
	elev1 = elev(name)
	elev1.sendHand()






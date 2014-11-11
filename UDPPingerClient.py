import time
from socket import *

from time import strftime

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)

ping = 0

while (ping < 10):
	ping = ping + 1
	start = time.clock()
	message = "Ping " + str(ping) + " " + str(strftime("%Y-%m-%d %H:%M:%S"))
	clientSocket.sendto(message, (serverName, serverPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print modifiedMessage.strip(), "\n", serverAddress

		elapsed = ((time.clock() - start) * 1000)
		print elapsed, " ms round trip"
	except:
		print "Request timed out for Packet #", ping
clientSocket.close()


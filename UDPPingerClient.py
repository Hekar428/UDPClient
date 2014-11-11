import time
from socket import *

from time import strftime

#Set serverName and Port
serverName = "localhost"
serverPort = 12000

#Bind socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Some variables for finding min, max, average and packet loss rate
min_trip = 0.0
max_trip = 0.0
average_trip = 0.0

packet_lost = 0.0
total_packets = 0.0

#Set timeout to one second
clientSocket.settimeout(1)

ping = 0

while (ping < 10):
	ping = ping + 1
	start = time.clock()
	message = "Ping " + str(ping) + " " + str(strftime("%H:%M:%S"))
	clientSocket.sendto(message, (serverName, serverPort))
	try:
		message, serverAddress = clientSocket.recvfrom(2048)
		print message

		elapsed = ((time.clock() - start) * 1000)
		print elapsed, "ms round trip"
		if elapsed < min_trip or min_trip == 0.0:
			min_trip = elapsed
		if elapsed > max_trip or max_trip == 0.0:
			max_trip = elapsed
		average_trip = average_trip + elapsed
	except:
		packet_lost = packet_lost + 1.0
		print "Request timed out"
	total_packets = total_packets + 1.0
	print ''
clientSocket.close()
print "Round Trip Time: max-> " + str(max_trip) + " min-> " + str(min_trip) + " average-> " + str(average_trip/total_packets)
print "Packet Loss Percentage: " + str(packet_lost/total_packets * 100) + "%"

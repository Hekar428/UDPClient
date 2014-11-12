import time
from time import strftime
from socket import *

#Set serverName and Port
serverName = "localhost"
serverPort = 50110

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
#loop 10 times
while (ping < 10):
	ping = ping + 1
	#start timer
	start_timer = time.clock()
	#set message format
	message = "Ping " + str(ping) + " " + str(strftime("%H:%M:%S"))
	clientSocket.sendto(message, (serverName, serverPort))
	try:
		#packet success print message with time
		message, serverAddress = clientSocket.recvfrom(2048)
		print message

		time_elapsed = ((time.clock() - start_timer) * 1000)
		print time_elapsed, "ms round trip"
		if time_elapsed < min_trip or min_trip == 0.0:
			min_trip = time_elapsed
		if time_elapsed > max_trip or max_trip == 0.0:
			max_trip = time_elapsed
		average_trip = average_trip + time_elapsed
	except: 
		#packet lost, print error.
		packet_lost = packet_lost + 1.0
		print "Request timed out"
	total_packets = total_packets + 1.0
	print ''
clientSocket.close()
#print out min, max, average, and packet loss percentage (extra assignment)
print "Round Trip Time: max-> " + str(max_trip) + " min-> " + str(min_trip) + " average-> " + str(average_trip / total_packets)
print "Packet Loss Percentage: " + str(packet_lost/total_packets * 100) + "%"

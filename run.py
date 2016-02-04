from Socket import openSocket, sendMessage
from initialize import joinRoom
from read import getUser, getMessage
import string


s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
	
	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		print(line)

		
		if line == "PING :tmi.twitch.tv":
			print("THIS WAS A PING!!" + line)
			s.send("PONG :tmi.twitch.tv\r\n")
			print("sent PONG")
		user = getUser(line)
		message = getMessage(line)
		print(user + " typed: " + message)

		if "!owner" in message:
			sendMessage(s, "duussk made this bot yo!")


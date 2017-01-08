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
		if line == "PING :tmi.twitch.tv":
			s.send("PONG :tmi.twitch.tv\r\n")
		user = getUser(line)
		message = getMessage(line)

		if "!owner" in message:
			sendMessage(s, "duussk made this bot yo!")


import config
import socket
import re

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

s = socket.socket()
s.connect((config.HOST,config.PORT))

#send the oauthtocken, nick and channel to join
s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))



#receive ping from server and answer pong
while True:
	response = s.recv(1024).decode("utf-8")
	if response == "PING :tmi.twitch.tv\r\n":
		s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
	else:
		username = re.search(r"\w+",response).group(0)
		message = CHAT_MSG.sub("", response)
		print(username + ": " + message)
		for pattern in config.PATT:
			if re.match(pattern, message):
				ban(s, username)
				break
	sleep(1 / config.RATE)

def chat(sock, msg):
	sock.send("PRIVMSG #{} :{}".format(config.CHAN,msg))

def ban(sock, user):
	chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
	chat(sock, ".timeout {]".format(user,secs))

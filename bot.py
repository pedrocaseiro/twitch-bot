import cfg
import socket

s=socket.socket()
s.connect((HOST,PORT))

#send the oauthtocken, nick and channel to join
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))



#receive ping from server and answer pong
while True:
	response = s.recv(1024).decode("utf-8")
	if response == "PING :tmi.twitch.tv\r\n":
		s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
	else:
		print(response)
	sleep(1 / cfg.RATE)

def chat(sock, msg):
	sock.send("PRIVMSG #{} :{}".format(cfg.CHAN,msg))

def ban(sock, user):
	chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
	chat(sock, ".timeout {]".format(user,secs))

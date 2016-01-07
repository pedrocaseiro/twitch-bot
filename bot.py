def chat(sock, msg):
	sock.send("PRIVMSG #{} :{}".format(cfg.CHAN,msg))

def ban(sock, user):
	chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
	chat(sock, ".timeout {]".format(user,secs))

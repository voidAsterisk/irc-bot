import socket, string, time
import threading
import atexit
import sys
SERVER = 'irc.freenode.net'
PORT = 6667
NICKNAME = 'Asuka'
CHANNEL = ''
	
def send_data(IRC, command):
	IRC.send((command + '\n').encode())

def main():
	print("Program started.")
	sys.stdout.flush()
	global IRC
	IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created.")
	sys.stdout.flush()
	IRC.connect((SERVER, PORT))
	print("Socket connected.")
	sys.stdout.flush()
	t = threading.Thread(target = Listener)
	t.daemon = True
	t.start()
	while True:
		continue

def Listener():
	send_data(IRC, "USER "+NICKNAME+" 8 * :GH0STW4TCH")
	send_data(IRC, "NICK "+NICKNAME)
    #send_data(IRC, "LIST")
	while True:
		buffer = IRC.recv(1024)
		if (len(buffer) == 0): continue
		print(buffer)
		sys.stdout.flush()
		msg = buffer.split()
		if (len(msg) > 0):
			if msg[0] == "PING":
				IRC.send("PONG %s" % msg[1] + '\n')
	
			
if __name__== "__main__":
	main()
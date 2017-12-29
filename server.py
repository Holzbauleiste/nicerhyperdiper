import socket
import welcomemessage

# -*- coding: utf-8 -*-

class Server():
	def __init__(self, _port):
		self.conn = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
		self.setupsock(_port)
		self.list = Clients()
		self.run = True

	def setupsock(self, _port = 1717):
		self.host = ''
		self.port = _port
		self.conn.bind((self.host, self.port))
		#done!
	def ListenForPeers(self):
		self.conn.listen(20)
		while self.run:
			conn, addr = self.conn.accept()
			print(addr[0] + " Has joined")
			if not self.list.Doubles(addr[0]):
				self.list.addClient(conn, addr)
			print("ClientList:     ")
			print(self.list.ClientList)
			conn.send(self.WelcomeMessage())
	def WelcomeMessage(self):
		return '\033[91m' + '       Welcome to the official ChatRoulette Server' + '\n\n' + '\033[0m' + '     Use ' + '\033[1m' + 'help' + '\033[0m' + ' for further instructions' + '\033[0m'



	def shutdown(self):
		self.conn.close()

class Clients(Server):
	def __init__(self):
		self.ClientList = []

	def addClient(self, conn, addr):
		self.ClientList.append((conn, addr))

	def Doubles(self, addr):
		for i in self.ClientList:
			if i[1][0] == addr:
				print("Double!")
				return True
		return False




TestServer = Server(4814)
TestServer.ListenForPeers()
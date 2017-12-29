import socket
import welcomemessage
import thread

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
				#print("ClientList:     ")
				#print(self.list.ClientList)
				conn.send(self.WelcomeMessage())
				action = ActionHandler(conn, addr)
				thread.start_new_thread(action.ActionHandlerLoop())
				print("OK Multithread")

	def WelcomeMessage(self):
		return '\033[91m' + '       Welcome to the official ChatRoulette Server' + '\n\n' + '\033[0m' + '     Use ' + '\033[1m' + 'help' + '\033[0m' + ' for further instructions' + '\n\n'



	def shutdown(self):
		self.conn.close()

class ActionHandler(Server):
	def __init__(self, _conn, _addr):
		self.connected = True
		self.conn = _conn
		self.addr = _addr

	def ActionHandlerLoop(self):
		while self.connected:
			command = self.conn.recv(25)
			print(command)




class Clients(Server):
	def __init__(self):
		self.ClientList = []

	def addClient(self, conn, addr):
		self.ClientList.append((conn, addr))

	def Doubles(self, addr):
		for i in self.ClientList:
			if i[1][0] == addr:
				return True
		return False

	def updateList(self):
		for i in self.ClientList:
			print i[0]
			if i[0] == None:
				print("None")




TestServer = Server(4815)
TestServer.ListenForPeers()
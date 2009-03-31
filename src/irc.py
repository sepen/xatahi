#!/usr/bin/env python


import os
import sys
import socket
import string


class Irc:

	s, rbuffer, status = None, None, None
	host, port, channel = None, None, None
	nick, ident, realname = None, None, None

	def __init__ (self, host, port, channel, nick):
		self.rbuffer = ""
		self.status = "disconnected"
		self.host, self.port, self.channel = host, port, channel
		self.nick, self.ident, self.realname = nick, nick, nick
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def close(self):
		self.s.close()
		self.status = "disconnected"

	def read(self):
		if self.status == "connected" or "joined":
			self.rbuffer = self.s.recv(1024)
			if self.rbuffer != None:
				fields = self.rbuffer.split()
				if fields[0] == "PING":
					self.s.send("PONG " + fields[1])

	def send(self, string):
		if self.status == "connected" or "joined":
			self.s.send("%s\r\n", string)

	def connect(self):
		self.status = "disconnected"
		self.s.connect((self.host, self.port))
		self.s.send("NICK %s\r\n" % self.nick)
		self.s.send("USER %s %s * :%s\r\n" % (self.ident, self.host, self.realname))
		self.status = "connected"
		self.read()

	def join(self):
		self.s.send("JOIN %s\r\n" % self.channel)
		self.send_to_channel("lokooooooo")
		self.status = "joined"
		self.read()

	def send_to_channel(self, string):
		if self.status == "connected" or self.status == "joined":
			self.s.send("PRIVMSG %s :%s\r\n" % (self.channel, string))

# End of file

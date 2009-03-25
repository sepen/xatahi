#!/usr/bin/env python


import os
import sys
import socket
import string


class Irc:
	
	s, rbuffer = None, None
	host, port, channel = None, None, None
	nick, ident, realname = None, None, None
		
	def __init__ (self, host, port, channel, nick):
		self.s = socket.socket()
		self.rbuffer = ""
		self.host, self.port, self.channel = host, port, channel
		self.nick, self.ident, self.realname = nick, nick, nick
	
	def read(self):
		self.rbuffer = self.s.recv(1024)	
	
	def connect(self):
		self.s.connect((self.host, self.port))
		self.s.send("NICK %s\r\n" % self.nick)
		self.s.send("USER %s %s * :%s\r\n" % (self.ident, self.host, self.realname))
		
	def join(self):
		self.s.send("JOIN %s\r\n" % self.channel)
		self.s.send("PRIVMSG %s :%s\r\n" % (self.channel, "lokooooooo"))

# End of file

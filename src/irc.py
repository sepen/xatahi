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
		self.host, self.port, self.channel = host, port, channel
		self.nick, self.ident, self.realname = nick, nick, nick
	
	def connect(self):
		readbuffer = ""
		s = socket.socket( )
		s.connect((self.host, self.port))
		s.send("NICK %s\r\n" % self.nick)
		s.send("USER %s %s * :%s\r\n" % (self.ident, self.host, self.realname))
		readbuffer = s.recv(1024)
		self.rbuffer = readbuffer
		return

# End of file

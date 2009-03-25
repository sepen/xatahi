#!/usr/bin/env python

import os
import sys
import socket
import string

class Irc:
	
	s, host, port, channel = None, None, None, None
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
		s.send("JOIN %s\r\n" % self.channel)
		readbuffer = s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop( )
		for line in temp:
			out = ""
			line = string.rstrip(line)
			vect = string.split(line)
			# server ping pong
			if (vect[0] == "PING"):
				s.send("PONG %s\r\n" % vect[1])
			else:
				out = out + line
		self.s = s
		return out

# End of file

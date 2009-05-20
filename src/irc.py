#!/usr/bin/env python
#
# IRC Class for Xatahi


#import os
#import sys
import socket
import string
import time
import gtk
from threading import Thread
gtk.gdk.threads_init()


class Irc(Thread):

	xatahi = None
	s, status = None, None
	host, port, channel = None, None, None
	nick, ident, realname = None, None, None

	def __init__ (self, xatahi, host = "irc.freenode.org", port = 6667, nick = "xatahi"):
		self.xatahi = xatahi
		Thread.__init__(self)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setblocking(0)
		self.host, self.port = host, port
		self.nick, self.ident, self.realname = nick, nick, nick
		self.status = "stopped"

	def run(self):
		while self.xatahi.exit == 0:
			time.sleep(1)
			if self.status == "running" or self.status == "joined":
				buffer = None
				buffer = self.read()
				if buffer != None:
					gtk.gdk.threads_enter()
					self.xatahi.gui.append_to_textview(buffer)
					gtk.gdk.threads_leave()

	def quit(self):
		try:
			self.s.close()
		except Exception, e:
			print e
			pass
		self.status = "stopped"

	def read(self):
		buffer = None
		try:
			buffer = self.s.recv(1024)
		except Exception, e:
			print e
			pass
		if buffer != None:
			fields = buffer.split()
			if fields[0] == "PING":
				try:
					self.s.send("PONG %s\r\n" % fields[1])
				except Exception, e:
					print e
					pass
				buffer = None				
		return buffer

	def send(self, string):
		self.s.send("%s\r\n", string)

	def connect_to_server(self):
		try:
			self.s.connect((self.host, self.port))
		except Exception, e:
			print e
			pass
		try:
			self.s.send("NICK %s\r\n" % self.nick)
			self.s.send("USER %s %s * :%s\r\n" % (self.ident, self.host, self.realname))
		except Exception, e:
			print e
			pass
		self.status = "running"

	def join_to_channel(self, channel = "#test"):
		try:
			self.s.send("JOIN %s\r\n" % channel)
		except Exception, e:
			print e
			pass
		self.channel = channel
		self.status = "joined"

	def send_to_channel(self, string):
		if self.status == "joined":
			try:
				self.s.send("PRIVMSG %s :%s\r\n" % (self.channel, string))
			except Exception, e:
				print e
				pass


# vim:ts=2 sw=2 noexpandtab
# End of file


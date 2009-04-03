#!/usr/bin/env python
#
# CommandLine Class for Xatahi

 
class CommandLine:

	# global vars
	xatahi = None

	def __init__(self, xatahi):
		self.xatahi = xatahi

	def do(self, line):
		args = line.split()
		if line == "/h" or line == "/help":
			self.show_help()
		elif line == "/s" or line == "/server":
			if self.xatahi.irc.status == "disconnected":
				self.xatahi.gui.append_to_textview("\n\n===> Connecting to %s at port %s...\n" % (self.xatahi.irc.host, self.xatahi.irc.port))
				self.xatahi.irc.connect_to_server()
			else:
				self.xatahi.gui.append_to_textview("**** You are connected to a server\n")
		elif line == "/q" or line == "/quit":
			self.xatahi.irc.quit()
		elif line == "/j" or line == "/join":
			if self.xatahi.irc.status == "connected" or self.xatahi.irc.status == "joined":
				self.xatahi.gui.append_to_textview("\n\n===> Joinning to %s as %s...\n" % ("#xatahi", self.xatahi.irc.nick))
				self.xatahi.irc.join_to_channel("#xatahi")
			else:
				self.xatahi.gui.append_to_textview("**** You must connect to a server\n")
		else:
			if self.xatahi.irc.status == "connected" or self.xatahi.irc.status == "joined":
				self.xatahi.gui.append_to_textview(">%s< %s\n" % (self.xatahi.irc.nick, line))
				self.xatahi.irc.send_to_channel(line)


# vim:ts=2 sw=2 noexpandtab
# End of file

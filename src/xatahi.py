#!/usr/bin/env python
#
# Xatahi: Tiny GTK2 client for IRC written in python


import commandline, irc, gui
from threading import Thread

 
class Xatahi:

	# global vars
	version = "0.1"
	exit = None
	commandline, irc, gui = None, None, None

	def __init__(self):
		self.exit = 0
		# create objects
		self.commandline = commandline.CommandLine(self);
		self.irc = irc.Irc(self, 'mikeux.dyndns.org', 6667, 'xatahi');
		self.gui = gui.Gui(self);
		# start the app
		self.gui.start()

	def quit(self):
		# call to quit
		self.irc.quit()
		self.gui.quit()


if __name__ == "__main__":
	x = Xatahi()


# vim:ts=2 sw=2 noexpandtab
# End of file

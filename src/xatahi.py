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
		self.irc = irc.Irc(self);
		self.gui = gui.Gui(self);
		# start threads
		self.irc.start()
		self.gui.start()

	def quit(self):
		self.exit = 1;
		# call to quit methods
		self.irc.quit();
		self.gui.quit();


if __name__ == "__main__":
	x = Xatahi()


# vim:ts=2 sw=2 noexpandtab
# End of file

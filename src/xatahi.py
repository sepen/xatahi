#!/usr/bin/env python
#
# Xatahi: Tiny GTK2 client for IRC written in python

 
import irc
import gui
from threading import Thread

 
class Xatahi:

	# global vars
	version = "v1.0"
	buffer = None
	irc, gui = None, None

	def __init__(self):
		# create objects
		self.irc = irc.Irc(self);
		self.gui = gui.Gui(self);
		# start threads
		self.irc.start()
		self.gui.start()

	def quit(self):
		# wait for threads
		#self.irc.join()
		#self.gui.join()
		# call to quit methods
		self.irc.quit();
		self.gui.quit();


if __name__ == "__main__":
	x = Xatahi()


# vim:ts=2 sw=2 noexpandtab
# End of file

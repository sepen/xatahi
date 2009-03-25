#!/usr/bin/env python
#
# Xatahi: Tiny GTK2 client for IRC written in python

 
import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
import irc

 
class Xatahi:

	wTree, irc, textview, textentry = None, None, None, None

	def __init__(self):
		self.wTree = gtk.glade.XML("xatahi.glade")
		self.wTree.signal_autoconnect(self)
		self.wTree.get_widget("window1").show_all()
		self.textview = self.wTree.get_widget("textview1")
		self.textbuffer = self.textview.get_buffer()
		self.textentry = self.wTree.get_widget("entry1")
		self.show_help()
		self.show_irc_connection()

	def show_help(self):
		infile = open("help.txt", "r")
		if infile:
			string = infile.read()
			infile.close()
			self.textbuffer.set_text(string)

	def show_irc_connection(self):
		self.textentry.set_text("Type: /server servername.domain")
		#self.irc = irc.Irc("mikeux.dyndns.org", 6667, "#mikeux", "xatahi")
		#self.irc.connect()
		#string = self.irc.rbuffer
		#textbuffer.set_text(string)

	def on_window1_delete_event(self, widget, event):
		gtk.main_quit()


if __name__ == "__main__":
	x = Xatahi()
	gtk.main()

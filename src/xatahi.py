#!/usr/bin/env python
#
# Xatahi: Tiny GTK2 client for IRC written in python

 
import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
import irc

 
class Xatahi:

	wTree, irc, textentry, textentrycontents = None, None, None, None
	textview, textbuffer, textviewcontents = None, None, None

	def __init__(self):
		self.wTree = gtk.glade.XML("xatahi.glade")
		self.wTree.signal_autoconnect(self)
		self.wTree.get_widget("window1").show_all()
		self.textentry = self.wTree.get_widget("entry1")
		self.textview = self.wTree.get_widget("textview1")
		self.textbuffer = self.textview.get_buffer()
		self.textentrycontents = ""
		self.textviewcontents = ""
		self.irc = irc.Irc("mikeux.dyndns.org", 6667, "#mikeux", "xatahi")
		#self.show_help()
		#self.irc_connect()
		#self.irc_join()

	def show_help(self):
		infile = open("help.txt", "r")
		if infile:
			string = infile.read()
			infile.close()
			self.append_to_textview(string)

	def append_to_textview(self, line):
		self.textviewcontents = self.textviewcontents + line
		self.textbuffer.set_text(self.textviewcontents)

	def on_entry1_enter_pressed(self, widget):
		self.textentrycontents = widget.get_text()
		widget.set_text("")
		self.append_to_textview(">%s< %s\n" % (self.irc.nick, self.textentrycontents))

	def irc_connect(self):
		self.irc.connect()
		self.irc.read()
		self.append_to_textview("\n\nConnecting to %s at port %s...\n" % (self.irc.host, self.irc.port))

	def irc_join(self):
		self.irc.join()
		self.irc.read()
		self.append_to_textview(self.irc.rbuffer)
		self.append_to_textview("Now talking on: %s\n" % self.irc.channel)

	def on_window1_delete_event(self, widget, event):
		gtk.main_quit()


if __name__ == "__main__":
	x = Xatahi()
	gtk.main()

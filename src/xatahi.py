#!/usr/bin/env python
#
# Xatahi: Tiny GTK2 client for IRC written in python

 
import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
import irc

 
class Xatahi:

	wTree, irc, t = None, None, None
	textentry, textentrycontents = None, None
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
		self.irc = irc.Irc("mikeux.dyndns.org", 6667, "#test", "xatahi")

	def show_help(self):
		infile = open("help.txt", "r")
		if infile:
			string = infile.read()
			infile.close()
			self.append_to_textview(string)

	def on_window1_delete_event(self, widget, event):
		self.irc.close()
		gtk.main_quit()

	def append_to_textview(self, line):
		self.textviewcontents = self.textviewcontents + line
		self.textbuffer.set_text(self.textviewcontents)

	def on_entry1_enter_pressed(self, widget):		
		self.textentrycontents = widget.get_text()
		if self.textentrycontents != None:
			widget.set_text("")
			self.do_tasks(self.textentrycontents)

	def do_tasks(self, string):
		if string == "/h" or string == "/help":
			self.show_help()
		elif string == "/s" or string == "/server":
			if self.irc.status == "disconnected":
				self.connect_to_server()
			else:
				self.append_to_textview("**** You are connected to a server\n")
		elif string == "/q" or string == "/quit":
			self.irc.close()
			gtk.main_quit()
		elif string == "/j" or string == "/join":
			if self.irc.status == "connected" or self.irc.status == "joined":
				self.join_to_channel()
			else:
				self.append_to_textview("**** You must connect to a server\n")
		else:
			if self.irc.status == "connected" or self.irc.status == "joined":
				self.append_to_textview(">%s< %s\n" % (self.irc.nick, string))
				self.irc.send_to_channel(string)

	def connect_to_server(self):
		self.append_to_textview("\n\n===> Connecting to %s at port %s...\n" % (self.irc.host, self.irc.port))
		self.irc.connect()
		self.append_to_textview(self.irc.rbuffer)

	def join_to_channel(self):
		self.irc.join()
		self.append_to_textview(self.irc.rbuffer)
		self.append_to_textview("===> Now talking on: %s\n" % self.irc.channel)


if __name__ == "__main__":
	x = Xatahi()
	gtk.main()

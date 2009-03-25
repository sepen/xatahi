#!/usr/bin/env python
#
# Xatahi: Tiny GTK2 client for IRC written in python

 
import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
import irc

 
class Xatahi:
	
	def __init__(self):
		self.glade = gtk.glade.XML("xatahi.glade")
		self.glade.signal_autoconnect(self)
		self.glade.get_widget("window1").show_all()
		
	def on_window1_delete_event(self, widget, event):
		gtk.main_quit()


if __name__ == "__main__":
	x = Xatahi()
	i = irc.Irc("mikeux.dyndns.org", 6667, "#mikeux", "xatahi")
	i.connect()
	gtk.main()

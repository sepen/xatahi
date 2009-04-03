#!/usr/bin/env python
#
# GUI Class for Xatahi

 
import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
from threading import Thread


class Gui(Thread):

	xatahi = None
	wTree = None
	textentry, textentrycontents = None, None
	textview, textbuffer, textviewcontents = None, None, None

	def __init__(self, xatahi):
		self.xatahi = xatahi
		Thread.__init__(self)
		self.wTree = gtk.glade.XML("xatahi.glade")
		self.wTree.signal_autoconnect(self)
		self.wTree.get_widget("window1").show_all()
		self.textentry = self.wTree.get_widget("entry1")
		self.textview = self.wTree.get_widget("textview1")
		self.textbuffer = self.textview.get_buffer()
		self.textentrycontents = ""
		self.textviewcontents = ""

	def run(self):
		gtk.main()

	def quit(self):
		gtk.main_quit()

	def show_help(self):
		infile = open("help.txt", "r")
		if infile:
			string = infile.read()
			infile.close()
			self.append_to_textview(string)

	def on_window1_delete_event(self, widget, event):
		self.xatahi.quit()

	def append_to_textview(self, line):
		self.textviewcontents = self.textviewcontents + line
		self.textbuffer.set_text(self.textviewcontents)

	def on_entry1_enter_pressed(self, widget):
		self.textentrycontents = widget.get_text()
		if self.textentrycontents != None:
			widget.set_text("")
			self.do_tasks(self.textentrycontents)

	def do_tasks(self, line):
		string = line
		self.xatahi.commandline.do(line)


# vim:ts=2 sw=2 noexpandtab
# End of file

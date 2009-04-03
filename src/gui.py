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
	textentry, textview, textbuffer = None, None, None

	def __init__(self, xatahi):
		self.xatahi = xatahi
		Thread.__init__(self)
		self.wTree = gtk.glade.XML("xatahi.glade")
		self.wTree.signal_autoconnect(self)
		self.wTree.get_widget("window1").show_all()
		self.textentry = self.wTree.get_widget("entry1")
		self.textview = self.wTree.get_widget("textview1")
		self.textbuffer = self.textview.get_buffer()

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
		pos = self.textbuffer.get_end_iter()
		self.textbuffer.insert(pos, line)
		self.textview.scroll_to_mark(self.textbuffer.get_insert(), 0)

	def on_entry1_enter_pressed(self, widget):
		line = widget.get_text()
		if line != None:
			widget.set_text("")
			self.do_tasks(line)

	def do_tasks(self, line):
		self.xatahi.commandline.do(line)


# vim:ts=2 sw=2 noexpandtab
# End of file

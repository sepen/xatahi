#!/usr/bin/env python
 
import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
 
class App:
	def __init__(self):
		self.glade = gtk.glade.XML("xatahi.glade")
		self.glade.signal_autoconnect(self)
		self.glade.get_widget("window1").show_all()
		
	def on_window1_delete_event(self, widget, event):
		gtk.main_quit()
	
	def on_button1_clicked(self, widget):
		gtk.main_quit()
 
if __name__ == "__main__":
	try:
		a= App()
		gtk.main()
	except KeyboardInterrupt:
		pass

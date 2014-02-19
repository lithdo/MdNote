#!/usr/bin/python3

from gi.repository import Gtk

class MdEditor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MdNote")
        
        self.set_default_size(800, 600)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        
        self.create_textview()
        
    def create_textview(self):
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.grid.attach(scrolled_window, 0, 0, 1, 1)
        
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(self.textview)
        
editor = MdEditor()
editor.connect("delete-event", Gtk.main_quit)
editor.show_all()
Gtk.main()

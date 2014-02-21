#!/usr/bin/python3

from gi.repository import Gtk, Gio
import sys

class MdEditorWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="MdEditor", application=app)

        self.set_default_size(800, 600)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.grid.attach(scrolled_window, 0, 0, 1, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(self.textview)

class MdEditor(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        self.win = MdEditorWindow(self)
        self.win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        menu = Gio.Menu()
        menu.append("New", "app.newfile")
        menu.append("Open", "app.openfile")
        menu.append("Save", "app.savefile")

        quit_menu = Gio.Menu()
        quit_menu.append("Quit", "app.quit")

        menu.append_section("",quit_menu)

        self.set_app_menu(menu)

        newfile_action = Gio.SimpleAction.new("newfile", None)
        newfile_action.connect("activate", self.on_menu_file_new)
        self.add_action(newfile_action)

        openfile_action = Gio.SimpleAction.new("openfile", None)
        openfile_action.connect("activate", self.on_menu_file_open)
        self.add_action(openfile_action)

        savefile_action = Gio.SimpleAction.new("savefile", None)
        savefile_action.connect("activate", self.on_menu_file_save)
        self.add_action(savefile_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_menu_file_quit)
        self.add_action(quit_action)

    def on_menu_file_new(self, action, parameter):
        print("New file")

    def on_menu_file_open(self, action, parameter):
        dialog = Gtk.FileChooserDialog("Open File...", self.win,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL,  Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN,    Gtk.ResponseType.OK))

        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("File selected: " + dialog.get_filename())
            fileopen = open(dialog.get_filename())
            self.win.textbuffer.set_text(fileopen.read())

        dialog.destroy()

    def on_menu_file_save(self, action, parameter):
        print("Save file")

    def on_menu_file_quit(self, action, parameter):
        self.quit()
            
app = MdEditor()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

#!/usr/bin/python3

from gi.repository import Gtk, Gio

UI_INFO = """
<ui>
    <menubar name='MenuBar'>
        <menu action='FileMenu'>
            <menuitem action='FileNew' />
            <menuitem action='FileOpen' />
            <menuitem action='FileSave' />
            <menuitem action='FileQuit' />
        </menu>
    </menubar>
</ui>
"""

class MdEditor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MdNote")

        self.set_default_size(800, 600)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        action_group = Gtk.ActionGroup("my_actions")
        self.add_file_menu_actions(action_group)

        uimanager = Gtk.UIManager()
        uimanager.add_ui_from_string(UI_INFO)
        uimanager.insert_action_group(action_group)

        menubar = uimanager.get_widget("/MenuBar")

        self.grid.attach(menubar, 0, 0, 1, 1)

        self.create_textview()

    def create_textview(self):
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.grid.attach(scrolled_window, 0, 1, 1, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(self.textview)

    def add_file_menu_actions(self, action_group):
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)

        action_filequit = Gtk.Action("FileNew", "New", None, None)
        action_filequit.connect("activate", self.on_menu_file_new)
        action_group.add_action(action_filequit)

        action_filequit = Gtk.Action("FileOpen", "Open", None, None)
        action_filequit.connect("activate", self.on_menu_file_open)
        action_group.add_action(action_filequit)

        action_filequit = Gtk.Action("FileSave", "Save", None, None)
        action_filequit.connect("activate", self.on_menu_file_save)
        action_group.add_action(action_filequit)

        action_filequit = Gtk.Action("FileQuit", "Quit", None, None)
        action_filequit.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_filequit)

    def on_menu_file_new(self, widget):
        print("New file")

    def on_menu_file_open(self, widget):
        print("Open file")

    def on_menu_file_save(self, widget):
        print("Save file")

    def on_menu_file_quit(self, widget):
        Gtk.main_quit()

editor = MdEditor()
editor.connect("delete-event", Gtk.main_quit)
editor.show_all()
Gtk.main()

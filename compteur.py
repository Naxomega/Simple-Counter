# _____       _        _          _____                               
#|     |___ _| |___   | |_ _ _   |   | |___ _ _ ___ _____ ___ ___ ___ 
#| | | | .'| . | -_|  | . | | |  | | | | .'|_'_| . |     | -_| . | .'|
#|_|_|_|__,|___|___|  |___|_  |  |_|___|__,|_,_|___|_|_|_|___|_  |__,|
#                         |___|                              |___|    
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

var = 0


class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Counter")

        global var
        
        # Create a Box container to hold widgets
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(box)  # Add the box to the window
        self.set_size_request(190, 30)

        self.button = Gtk.Button(label="-")
        self.button.connect("clicked", self.moins)
        self.button.set_size_request(70, 30)  # Width: 40 pixels, Height: 30 pixels
        box.pack_start(self.button, False, False, 0)  # Don't expand or fill

        self.label = Gtk.Label(label="0", angle=0, halign=Gtk.Align.CENTER)
        box.pack_start(self.label, True, True, 0)  # Add label to the box
        self.button1 = Gtk.Button(label="+")
        self.button1.connect("clicked", self.plus)
        self.button1.set_size_request(70, 30)  # Same size as the other button
        box.pack_start(self.button1, False, False, 0)  # Don't expand or fill
        

    def plus(self, widget):
        global var
        var = var + 1
        
        self.label.set_text(f"{var}")  # Update the label text
    def moins(self, widget):
        global var
        var = var - 1
        
        self.label.set_text(f"{var}")  # Update the label text

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
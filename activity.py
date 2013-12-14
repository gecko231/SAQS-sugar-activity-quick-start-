# code your activity here
# or replace this file with your python activity file
# import statements

"""
class exampleActivity(activity.Activity):

"""


# Sugar Imports
from sugar3.activity.activity import Activity
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityButton


# Gtk Import
from gi.repository import Gtk
from gettext import gettext as _

class Example(Activity):
    def __init__(self, sugar_handle):
        Activity.__init__(self, sugar_handle)

        # Create a Toolbar
        toolbar = Gtk.Toolbar()

        # Add toolbar to Sugar Activity Toolbar Space
        self.set_toolbar_box(toolbar)

        # Add Activity Button
        toolbar.insert(ActivityButton(self), -1)

        # Create & Add Separator
        separator = Gtk.SeparatorToolItem(draw=False)
        separator.set_expand(True)
        toolbar.insert(separator, -1)

        # Add Stop Button
        toolbar.insert(StopButton(self), -1)

        # Create Container
        grid = Gtk.Grid()

        # Add grid to Sugar Activity GtkWindow
        self.set_canvas(grid)

        # Create & Add Label
        label = Gtk.Label(label=_("Weather: "))
        grid.attach(label, 0, 0, 1, 1)

        # Add Output Label
        output = Gtk.Label()
        grid.attach(output, 0, 6, 1, 1)

        # Create & Add Text Entry x2
        entry = Gtk.Entry()
        grid.attach(entry, 0, 1, 1, 1)
        entry2 = Gtk.Entry()
        grid.attach(entry2, 0, 2, 1, 1)

        # Empty output on keypress in entry
        entry.connect('key-release-event', self.emptyout, output)
        entry2.connect('key-release-event', self.emptyout, output)

        # Add buttons
        sunnyButton = Gtk.Button(label=_("<sunny>"))
        grid.attach(sunnyButton, 0, 3, 1, 1)
        
        buttyButton = Gtk.Button(label=_("<butty>"))
        grid.attach(buttyButton, 1, 3, 1, 1)

        rainyButton = Gtk.Button(label=_("<rainy>"))
        grid.attach(rainyButton, 2, 3, 1, 1)

        snowyButton = Gtk.Button(label=_("<snowy>"))
        grid.attach(snowyButton, 3, 3, 1, 1)

        # Tell the buttons to run a class method
        sunnyButton.connect('clicked', self.showWeather, "Sunny", entry, entry2, output)
        buttyButton.connect('clicked', self.showWeather, "Butty", output)
        rainyButton.connect('clicked', self.showWeather, "Rainy", output)
        snowyButton.connect('clicked', self.showWeather, "Snowy", output)

        # Show all components (otherwise none will be displayed)
        self.show_all()

    def greeter(self, button, entry, entry2, output):
        if len(entry.get_text()) > 0:
            output.set_text("WEATHER TODAY IS: \n" + entry.get_text() + "\n" + entry2.get_text())
        else:
            output.set_text("Enter the weather.")

    def showWeather(self, button, state, entry, entry2, output):
        output.set_text("Weather State is: " + state + ". " + "Temperature is " + entry.get_text() + ". Humidity is " + entry2.get_text())

    def emptyout(self, entry, entry2, event, output):
        output.set_text("")

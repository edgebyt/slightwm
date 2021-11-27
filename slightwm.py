from Xlib import X, XK
from Xlib.display import Display

from keyboard import keyboard
from map import mapping

class winman:
    def __init__(self):
        self.display = Display()
        self.rootWin = self.display.screen().root

        self.rootWin.change_attributes(event_mask = X.SubstructureRedirectMask)

        self.keyboardHandler = keyboard(self.display, self.rootWin)
        self.mappingHandler = mapping(self.display, self.rootWin)

    def eventHandler(self):
        if self.display.pending_events() > 0:
            event = self.display.next_event()
            print("Event: ".format(str(event.type)))
            if event.type == X.KeyPress: self.keyboardHandler.handleKeyEvent(event)
            elif event.type == X.MapRequest: self.mappingHandler.mapHandler(event)

    def loop(self):
        while True:
            self.eventHandler()
            self.updateFocus()

windowManager = winman()
windowManager.loop()

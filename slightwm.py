from Xlib import X, XK
from Xlib.display import Display

class winman:
    def __init__(self):
        self.display = Display()
        self.rootWin = self.display.screen().root

        self.rootWin.change_attributes(event_mask = X.SubstructureRedirectMask)

    def eventHandler(self):
        if self.display.pending_events() > 0:
            event = self.display.next_event()
            print("Event: ".format(str(event.type)))

    def loop(self):
        while True:
            self.eventHandler()

windowManager = winman()
windowManager.loop()

from Xlib import X, XK
from utils import runProcess

class keyboard:
    def __init__(self, display, rootWin):
        self.display = display
        self.rootWin = rootWin
        self.configKeys()

    def configKeys(self):
        grabbedKeys = [[X.Mod1Mask, XK.XK_T], [X.Mod1Mask, XK.XK_E], [X.NONE, X.Mod1Mask]]
        for keyBinding in grabbedKeys:
            modifier = keyBinding[0]
            key = keyBinding[1]
            codes = getKeys(key)
            for code in codes:
                self.rootWin.grab_key(code, modifier, 1, X.GrabModeAsync, X.GrabModeAsync)

    def getKeys(self, key):
        codes = set(code for code, index in self.display.keysym_to_keycodes(key))
        return codes

    def keyHandler(self, event):
        if event.detail in self.getKeys(XK.XK_T): runProcess("/usr/bin/kitty")

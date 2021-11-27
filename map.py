from Xlib import X

class mapping:
    def __init__(self, display, rootWin):
        self.display = display
        self.winList = []

    def mapHandler(self, event):
        event.window.map()
        event.window.set_input_focus(X.RevertToParent, X.CurrentTime)
        event.window.configure(stack_mode = X.Above)
        self.winList.append(event.window)

    def unmapHandler(self, event):
        event.window.unmap()
        self.winList.remove(event.window)

    def updateFocus(self):
        self.focusedWindow = self.display.get_input_focus()

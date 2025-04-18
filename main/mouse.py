from ..main.engine import Base
from pygame import Vector2, mouse, MOUSEWHEEL


class MouseButton:
    def __init__(self):
        self.Pressed = False
        self.Held = False
        self.Released = False
        self.HoldTime = 0
        self.PreviousHoldTime = 0

    def update(self, pressed, engine):
        if self.Released:
            self.Released = False

        if self.Held and not pressed:
            self.Held = False
            self.Released = True

        if self.Held:
            self.HoldTime += engine.Runtime.getTime() / 1000

        if self.Pressed and pressed:
            self.Pressed = False

        if not self.Pressed and pressed and not self.Held:
            self.Pressed = True
            self.Held = True
            self.PreviousHoldTime = self.HoldTime
            self.HoldTime = 0

    def __str__(self):
        return f"[Pressed: {self.Pressed} | Held: {self.Held} | Released: {self.Released} | HoldTime: {self.HoldTime} | PreviousHoldTime: {self.PreviousHoldTime}] "


class Mouse(Base):
    def __init__(self):
        super().__init__()

        self.Scroll = 0

        self.Pos = Vector2(0,0)
        self.Delta = Vector2(0,0)

        self.LMB = MouseButton()
        self.RMB = MouseButton()
        self.MMB = MouseButton()
        self.Engine.Events.insertEventSentEvent(MOUSEWHEEL, self._getScroll)

    def _getScroll(self, event):
        self.Scroll = event.precise_y

    def update(self):
        self.Pos = Vector2(mouse.get_pos())
        self.Delta = Vector2(mouse.get_rel())

        pressed = mouse.get_pressed()

        self.LMB.update(pressed[0], self.Engine)
        self.MMB.update(pressed[1], self.Engine)
        self.RMB.update(pressed[2], self.Engine)

        self.Scroll = 0

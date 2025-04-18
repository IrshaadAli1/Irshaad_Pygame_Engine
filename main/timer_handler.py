from ..timer import Timer

class Sequence(list):
    def __init__(self):
        list.__init__(self)

    def addTimer(self, timer: Timer):
        self.append(timer)

    def update(self):
        if len(self) <= 0: return
        timer = self[0]
        timer.update()

        if timer.Repeat == 0:
            self.pop(0)


class TimerGroup(list):
    def __init__(self):
        list.__init__(self)

    def addTimer(self, timer: Timer):
        self.append(timer)

    def update(self):
        if len(self) <= 0: return
        for timer in self[:]:
            timer.update()

            if timer.Repeat == 0:
                self.pop(self.index(timer))

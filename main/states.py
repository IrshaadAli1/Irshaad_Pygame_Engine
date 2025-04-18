from .function_database import SetFunction


class States(dict):
    def __init__(self):
        super().__init__(
            Main=SetFunction(lambda: print("ENTER A MAIN STATE!"))
        )

        self.CurState = "Main"

    def setState(self, state: str, func: SetFunction):
        self[state] = func or SetFunction(lambda: None)

    def getState(self, state: str):
        return self.get(state, None)

    def runCurState(self):
        self.get(self.CurState, (lambda: print("ENTER A MAIN STATE!")))()

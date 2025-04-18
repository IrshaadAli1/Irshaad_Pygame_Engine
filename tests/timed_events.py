from engineV3 import Engine, Timer, SetFunction

engine = Engine()
engine.Sequence.addTimer(Timer(1, 2, SetFunction(lambda: print("hello world")), 2))

engine.mainState = None
engine.run()
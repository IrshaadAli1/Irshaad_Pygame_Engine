from engineV3 import Engine


engine = Engine()

def main():
    engine.Window.position = (engine.Window.position[0] + 1, engine.Window.position[1] + 1)
    ...

engine.mainState = main
engine.run()
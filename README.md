# Irshaad's Pygame Engine!
An engine to help new people to pygame have a bit more fun with creating!

Version - V3
Date - 18/04/2025

# What requirements are needed to install?
Suggested to install the following pip packages = [
  "pygame-ce",
  "lxml",
  "multipledispatch",
  "pydub" ( should already be implemented in the engine )
]

## Installation
Dependencies - Install pygame-ce and lxml
```bash
pip install pygame-ce
pip install lxml
```
The Engine - Just download it, and import it and you should be good to go!
```python
from engineV3 import Engine

e = Engine()


def main():
  ...

e.mainState = main
e.run()
```

## Usage
### Engine
Written on 18/04/2025
#### Engine - Main
Contains the Base class, which will implement the Engine class as a subclass

The Engine Class has many modules which make it an engine such as Runtime, Event Handler, States, Timer Handler, Tween Handler, Mouse, Keyboard, Camera
#### Engine - Runtime
Currently just acts as the pygame.time.Clock module, but with a settable framerate.

#### Engine - Event Handler
The Event Handler has 4 types of core events:
  > Regular: If event then call function (automatically implements QUIT)
  > EventSent: If event then call function with event as arg
  > KeyDown: If event is keyDown, then if key is event key then call function
  > KeyUp: If event is keyUp then if key is event key then call function

#### Engine - States
The State contains multiple functions you can call to use as states, with "Main" being MainState which is automatically called by the engine on start.

#### Engine - Timer Handler
##### Engine - Timer Handler - Sequence
Calls functions in the order it is given, moving one by one through a set time.

```python
e.Sequence.addTimer(Timer(2, 4, SetFunction(print, "Hello", "World!"), 3))  # Waits 2 seconds before printing "Hello World!" every 4 seconds, 3 times before moving onto the next timer function
```

##### Engine - Timer Handler - TimerGroup
Calls function with no order other than the time until it is called.

```python
# t1 has func called at 1 second interval 2 times
# t2 has func called at 2 second interval 2 times
# s"x" = x seconds

e.TimerGroup.addTimer(t1)
e.TimerGroup.addTimer(t2)

# timers called at s"x" -> s1: t1, s2: [t1, t2], s3: None, s4: t2, s5: None, s6: None
```

#### Engine - Tween Handler
Nothing cool here keep scrolling

#### Engine - Mouse
The mouse package for pygame. Supports LMB, MMB, RMB mouse presses with each one having a hold time as well  as check if pressed, released, and held.

```python
e.Mouse.LMB.Pressed
e.Mouse.RMB.Held
```

also supports vertical scrolling

```python
e.Mouse.Scroll
```

and Position and Delta

```python
e.Mouse.Position
e.Mouse.Delta
```

#### Engine - Input
Supports every pygame/pygame-ce key in pygame.constants that starts with "K_"
Checks if pressed, held, released, and has hold time.

```python
e.Input["k"]  # Gets the Key class of the certain key using the __getitem__ method
e.Input["k"].Pressed  # Checks if "k" key is pressed

e.Input["k", "C"].Pressed  # Checks if any key given is pressed
e.Input[any, "k", "c"].Pressed  # Checks if any key given is pressed
e.Input[all, "k", "c"].Pressed  # Checks if all keys given is pressed

e.Input[any, "k", "c"].HoldTime  # Gets the max hold time of the keys given
e.Input[all, "k", "f", "c"].HoldTime  # Gets the min hold time of the keys given (and the max wait time for a bucket of fried chicken)
```
#### Engine - Camera
Camera Support! Now you can do things like splitscreen!

You can blit images/sprites to the screen

```python
e.MainCamera.render(Sprite1, Sprite2, Sprite3)
e.MainCamera.blitSurface(sf1, sf2, sf3)
```

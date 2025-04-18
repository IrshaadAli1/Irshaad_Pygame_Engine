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

# How to use?
Just download it, and import it and you should be good to go!

# Features:
  # Main:
    > Contains 2 Classes - Base and Engine
    > Engine - Runtime:
      > Uses the clock method and a settable framerate
    > Engine - States:
      > Contains a Main State which you will be annoyed via looped prints until you set it to None or a SetFunction
      > Can switch between different States
    > Engine - Function Database:
      > SetFunction - On calling, will call the function with it's args and kwargs set
    > Engine - Event Handler:
      > Uses pygame/pygame-ce events in order to quit the program
      > Able to set KeyDown/KeyUp events
      > Able to set event functions which also uses the event as the argument
      > Set events
    > Engine - Timer Handler:
      > Sequence:
        >> Calls one function at a time with the given amount of time
        >> Is a SetFunction
      > Timer:
        >> Calls any amount of functions at a time with the given amount of time
        >> Is a SetFunction
    > Engine - Tween Handler:
      > Handles Tweening - nothing cool here
    > Engine - Mouse
      > Has LMB, RMB, MMB support
      > Scroll Wheel Support - Only vertically (ew horizontal - might add later)
      > Position and Delta
    > Engine - Mouse
      > Supports every key that starts with "K_" in pygame.constants (from pygame-ce)
      > Able to get key via the __getitem__ function
        >> Engine.Input["k"].Pressed  # Get a key state using the get item method
        >> Engine.Input["k", "a"].Pressed  # Check if any key given is pressed!
        >> Engine.Input[all, "k", "a"].Pressed # Check if all keys given is pressed!

        >> Engine.Input[all, "k", "a"].HoldTime  # If "k" is pressed and not "a" - Hold Time is 0. If "k" is pressed and then "a", it'll get the minimum hold time of the keys that are            pressed.
        >> Engine.Input[any, "k", "a"].HoldTime  # If "k" is pressed and not "a" - Hold time is "k"'s hold time. If both are pressed, it'll get the maximum hold time of the keys that             are pressed.
      > Engine - Camera
        > A Camera which you can use to create multiple displays of the same object (Eg: 4 player game shared across 1 screen)
        > Has Target selecting
        > World positioning
        > Zoom support
    

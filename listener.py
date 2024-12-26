import keyboard
import threading


# Access and print all available modifier keys
modifiers = keyboard.all_modifiers()
print("Available modifiers:")
print(modifiers)

# Access and print all available hotkeys
hotkeys = keyboard.all_hotkeys()
print("Available hotkeys:")
print(hotkeys)

# Remapper 
## Assign keyboard shortcut to any key of a keyboard.


This is especially useful for people with custom keyboards or people with Acer Nitro laptops or others with custom built in keys. 
* For custom keyboards, you could add new keys and assign shortcuts to them.
* For Acer Nitros, because we have a 'Nitro Sense' button which is mostly under-utilized and I don't think opening a simple app would warrant a separate button on the keyboard. So remapping it to a useful windows shortcut is what I did.
* I remapped my Nitro sense button to switch between two desktops. That is what the default code does.

## Usage Instructions
* ``` pip install keyboard ```
* Run the *listener.py* file, press your custom key/button and notedown its corresponding keycode which will be printed to the terminal.
* Enter the keycode in the *remapper.py* file, in the `CUSTOM_KEYCODE = 117` line change the 117 to your keycode.
* Change the keyboard shortcut in the `KEYBOARD_SHORTCUT = {}` line to your desired keyboard press or keyboard shortcut and save it.
* Run the *remapper.py* file to ensure that the custom key is working as intended.
* Run `pip install pyinstaller`
* Run `pyinstaller --noconsole --onefile remapper.py` to build your own executable that will run the background and simulate your keypresses.
* Run the *remapper.exe* file in the newly generated dist folder to run the executable file.
  
## `listener.py` is used to detect the custom keycode of your key/button.
## `remapper.py` has functionality to simulate shortcut/keypress and assign it to any keyboard key/button.
I also added additional mutex so that even if you mistakenly run the executable multiple times, only one executable persists in the background and the rest are killed. So you don't have to worry about multiple processes slowing down your PC.


:)

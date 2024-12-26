# Working prototype that switches between two desktops in windows
import keyboard
import time
import sys
import win32event
import win32api
import win32con
import win32process

mutex_name = "remapper"  # Use a unique name for your mutex

# Try to create a mutex
mutex = win32event.CreateMutex(None, 1, mutex_name)

# Check if the mutex is already taken
if win32api.GetLastError() == win32con.ERROR_ALREADY_EXISTS:
    print("Another instance of the application is already running.")
    sys.exit(0)  # Exit if mutex exists, i.e., app already running

print("Application is running...")


############################################################################## APP LOGIC HERE

# Define the custom keycode for the NitroSense button (replace with your keycode if you want to change any other key)
CUSTOM_KEYCODE = 117  # Custom keycode for the Acer nitro sense button.

# Define the keyboard shortcut to simulate (e.g., Ctrl+Alt+T for opening the terminal)
KEYBOARD_SHORTCUT = {1: ['win', 'ctrl', 'right'], 2: ['win', 'ctrl', 'left']}

# Function to simulate a keyboard shortcut
def simulate_shortcut(shortcut):
    for key in shortcut:
        keyboard.press(key)  # Press the key in the shortcut
    for key in shortcut:
        keyboard.release(key)  # Release the key in the shortcut

# Listen for the custom key press and simulate a shortcut when pressed
# print("Listening for custom key press (keycode: {})...".format(CUSTOM_KEYCODE))

prev = 0
while True:
    event = keyboard.read_event()  # Capture the key event

    # Check if the custom key is pressed based on its keycode
    if event.event_type == keyboard.KEY_DOWN and event.scan_code == CUSTOM_KEYCODE:
        # print("Custom key pressed! Simulating shortcut...")
        # print(f"prev = {prev}")
        if prev == 1:
            simulate_shortcut(KEYBOARD_SHORTCUT[2])  # Simulate the keyboard shortcut 2
            time.sleep(0.5)  # Sleep to prevent multiple presses in quick succession
            prev = 2
        elif prev == 2:
            simulate_shortcut(KEYBOARD_SHORTCUT[1])  # Simulate the keyboard shortcut 1
            time.sleep(0.5)  # Sleep to prevent multiple presses in quick succession
            prev = 1
        elif prev == 0:
            simulate_shortcut(KEYBOARD_SHORTCUT[1])  # Simulate the keyboard shortcut 1
            time.sleep(0.5)  # Sleep to prevent multiple presses in quick succession
            prev = 1
    
    # Optionally, exit the loop by pressing the 'esc' key
    # if event.name == 'esc':
        # print("Exiting the script.")
        # break

# Keep the application running so that the mutex doesn't get released
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

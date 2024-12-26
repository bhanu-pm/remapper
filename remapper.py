import keyboard
import time
import sys
import win32event
import win32api

# Mutex logic to ensure a single instance of the application
mutex_name = "nitro_remapper"  # Use a unique name for your mutex
mutex = win32event.CreateMutex(None, False, mutex_name)

# Check if the mutex already exists
if win32api.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
    sys.exit(0)  # Exit if another instance is running


########################################################     App logic
CUSTOM_KEYCODE = 117  # Custom keycode for the Acer NitroSense button
KEYBOARD_SHORTCUT = {1: ['win', 'ctrl', 'right'], 2: ['win', 'ctrl', 'left']}

# Function to simulate a keyboard shortcut
def simulate_shortcut(shortcut):
    for key in shortcut:
        keyboard.press(key)
    for key in shortcut:
        keyboard.release(key)

# Main function to handle remapping
def nitro_remapper_fn(prev):
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.scan_code == CUSTOM_KEYCODE:
        if prev == 1:
            simulate_shortcut(KEYBOARD_SHORTCUT[2])
            time.sleep(0.5)
            return 2
        elif prev == 2:
            simulate_shortcut(KEYBOARD_SHORTCUT[1])
            time.sleep(0.5)
            return 1
        elif prev == 0:
            simulate_shortcut(KEYBOARD_SHORTCUT[1])
            time.sleep(0.5)
            return 1
    return prev  # Return the unchanged state if no relevant event occurred

# Keep the application running so the mutex isn't released
try:
    prev = 0  # Initial state
    while True:
        try:
            prev = nitro_remapper_fn(prev)  # Pass the state and update it
        except Exception as e:
            # print(f"Error in remapper function: {e}")  # Log errors for debugging
            pass
except KeyboardInterrupt:
    # print("\nApplication stopped by user.")
    pass
except Exception as e:
    # print(f"Unexpected error: {e}")
    pass
finally:
    # print("Exiting application.")
    pass

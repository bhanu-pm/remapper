import keyboard
import time


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
print("Listening for custom key press (keycode: {})...".format(CUSTOM_KEYCODE))
while True:
    event = keyboard.read_event()  # Capture the key event

    # Check if the custom key is pressed based on its keycode
    if event.event_type == keyboard.KEY_DOWN and event.scan_code == CUSTOM_KEYCODE:
        print("Custom key pressed! Simulating shortcut...")
        simulate_shortcut(KEYBOARD_SHORTCUT)  # Simulate the keyboard shortcut
        time.sleep(0.5)  # Sleep to prevent multiple presses in quick succession
    
    # Optionally, exit the loop by pressing the 'esc' key
    if event.name == 'esc':
        print("Exiting the script.")
        break

# Code to find the key pressed and the keycode for the custom keyboard button.
import keyboard


# Print the name of the key when pressed
print("Press any key to see its name or keycode. Press 'esc' to exit.")

while True:
    event = keyboard.read_event()  # Capture keyboard events
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name} (Key code: {event.scan_code})")
    if event.name == 'esc':  # Exit on Escape key press
        break

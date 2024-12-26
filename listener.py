import keyboard

# Example: Check if a specific key is pressed
if keyboard.is_pressed('esc'):
    print("Esc key is pressed")

# Example: Print out key events as they happen
print("Listening for key events. Press 'Esc' to exit.")
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name}")
    elif event.event_type == keyboard.KEY_UP:
        print(f"Key released: {event.name}")
    if event.name == 'esc':
        break

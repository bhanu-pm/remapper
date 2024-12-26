import keyboard
import threading

# def log_keyboard_events():
#     """
#     Function to log all keyboard events.
#     Captures key press and release events and prints them to the console.
#     """
#     print("Keyboard event logging is active.")
#     print("Press 'Esc' to stop logging and exit the program.")

#     # Listen for all keyboard events
#     for event in keyboard.record(until='esc'):
#         if event.event_type == 'down':
#             print(f"Key Pressed: {event.name}")
#         elif event.event_type == 'up':
#             print(f"Key Released: {event.name}")


def main():
    """
    Function to remap shortcuts to specific keys.
    """
    def remapper():
        keyboard.press_and_release('None')

    # Add hotkeys for remapping
    keyboard.add_hotkey('win+ctrl+right', remapper)  # Replace Ctrl+Alt+P with Home
    keyboard.add_hotkey('win+ctrl+left', remapper)

    print("Shortcut remapping is active. Press Nitro for desktop change.")
    print("Press Esc to exit the program.")

    # Keep the remapping active until 'Esc' is pressed
    keyboard.wait('esc')


if __name__ == "__main__":
    # Run the main function and keyboard logger in parallel threads
    remapping_thread = threading.Thread(target=main, daemon=True)
    # logging_thread = threading.Thread(target=log_keyboard_events, daemon=True)

    remapping_thread.start()
    # logging_thread.start()

    # Keep the main script running
    try:
        remapping_thread.join()
        # logging_thread.join()
    except KeyboardInterrupt:
        print("\nExiting...")

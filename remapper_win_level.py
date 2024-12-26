import ctypes
import time


# Load user32.dll (handles user interactions like keyboard events)
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Define constants for keycodes (you can customize this as needed)
KEY_PRESSED = 0x8000  # Bit mask to check if the key is pressed
KEY_A = 0x41  # Key code for 'A'
KEY_B = 0x42  # Key code for 'B'

# Virtual key codes (you can add more as needed)
VIRTUAL_KEY_CODES = {
    'A': 0x41,  # 'A'
    'B': 0x42,  # 'B'
    'C': 0x43,  # 'C'
    'ENTER': 0x0D,  # Enter key
    'ESC': 0x1B,  # Escape key
    'SPACE': 0x20,  # Space bar
    'SHIFT': 0x10,  # Shift key
    'CTRL': 0x11,   # Control key
    'ALT': 0x12     # Alt key
}
def get_key_state(key_code):
    """
    Check if a particular key is pressed using GetAsyncKeyState.
    """
    # Get the state of the specified key
    # print(f"keycode is {user32.GetAsyncKeyState(key_code)} and keypressed is {KEY_PRESSED}")
    return user32.GetAsyncKeyState(key_code) & KEY_PRESSED


def press_key(key_code):
    """
    Simulate the pressing of a key using keybd_event.
    """
    # Simulate a key press (key down)
    user32.keybd_event(key_code, 0, 0, 0)
    # Simulate a key release (key up)
    user32.keybd_event(key_code, 0, 2, 0)


def remap_keys():
    """
    Continuously intercept key presses and remap them to alternate keys.
    """
    print("Running key remap script. Press 'Esc' to exit.")
    
    while True:
        # Intercept and check if 'A' is pressed
        if get_key_state(VIRTUAL_KEY_CODES['A']):
            print("Key 'A' pressed, remapping to 'B'.")
            press_key(VIRTUAL_KEY_CODES['B'])  # Simulate pressing 'B' instead
        
        # Intercept and check if 'B' is pressed
        if get_key_state(VIRTUAL_KEY_CODES['B']):
            print("Key 'B' pressed, remapping to 'A'.")
            press_key(VIRTUAL_KEY_CODES['A'])  # Simulate pressing 'A' instead
        
        # Stop when 'Esc' is pressed
        if get_key_state(VIRTUAL_KEY_CODES['ESC']):
            print("Exiting key remap script.")
            break
        
        # Sleep to reduce CPU usage while waiting for key press
        time.sleep(0.01)  # Adjust the delay as needed


if __name__ == "__main__":
    remap_keys()

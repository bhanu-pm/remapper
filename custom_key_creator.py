import keyboard

# Define a function that simulates pressing your custom key
def custom_key_function():
    print("Custom key pressed!")

# Define your custom key (let's call it 'f13' for this example)
keyboard.add_hotkey('end', custom_key_function)  # Remap F13 to your custom key function

print("Press F13 to trigger the custom key.")
keyboard.wait('esc')  # Press Esc to exit

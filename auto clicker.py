import pyautogui
import time
import sys
from pynput import keyboard  # Alternative library for key detection
from threading import Thread  # For running the listener in a separate thread

time_delay_btw_clicks = 0.01  # Delay between clicks (in seconds)
time_delay_each_round = 3     # Delay between rounds of clicking (in seconds)

# Global flag to check if the program should exit
exit_flag = False

# Define default coordinates. Update these values as needed.
default_coordinates = [(100, 200), (300, 400), (500, 600)]  # example default coordinates

def on_press(key):
    """Detect key presses and terminate the program if 'e' is pressed."""
    global exit_flag
    try:
        if key.char == 'e':  # Check if the key is 'e'
            print("\nExecution terminated by user.")
            exit_flag = True
            return False  # Stop the listener
    except AttributeError:
        pass

def start_key_listener():
    """Start a listener for the 'e' key in a separate thread."""
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def capture_coordinates(n):
    """Capture `n` mouse click coordinates."""
    print(f"Click on {n} spots to capture their coordinates.")
    print("Move the mouse to the desired position and press Enter to capture.")
    print("Press 'e' at any time to terminate the script.\n")

    coordinates = []
    for i in range(n):
        print(f"Waiting for click {i + 1}...")
        input("Press Enter when ready...")
        x, y = pyautogui.position()
        coordinates.append((x, y))
        print(f"Captured coordinates for click {i + 1}: {x, y}\n")

    print("\nAll coordinates captured:")
    for i, (x, y) in enumerate(coordinates, start=1):
        print(f"Click {i}: ({x}, {y})")
    
    return coordinates

def countdown_timer(seconds):
    """Countdown timer."""
    for i in range(seconds, 0, -1):
        if exit_flag:  # Check if exit_flag is set
            sys.exit()
        print(f"Starting in {i} seconds...", end='\r')
        time.sleep(1)
    print("Starting clicks now!")

def wait_until(target_time):
    """Wait until target_time (format: HH:MM:SS)."""
    print(f"Waiting until {target_time} to start clicking... Press 'e' to exit.")
    while time.strftime("%H:%M:%S", time.localtime()) < target_time:
        if exit_flag:  # Check if exit_flag is set
            sys.exit()
        time.sleep(1)
    print("Starting clicks now!")

def refresh_page():
    """Simulate Ctrl+R key press to refresh the page before clicking."""
    print("Refreshing the page (Pressing Ctrl + R)...")
    pyautogui.hotkey("ctrl", "r")  # Simulates pressing Ctrl + R
    time.sleep(time_delay_btw_clicks)  # Small delay to allow the page to refresh

def click_spots(coords, spam_mode):
    """Click at the given coordinates."""
    if spam_mode:
        print("Spam mode is active. Looping indefinitely...\n")
        while True:
            if exit_flag:  # Check if exit_flag is set
                sys.exit()
            for x, y in coords:
                pyautogui.click(x, y)
                time.sleep(time_delay_btw_clicks)
            time.sleep(time_delay_each_round)
    else:
        print("Clicking each spot once...\n")
        for x, y in coords:
            if exit_flag:  # Check if exit_flag is set
                sys.exit()
            pyautogui.click(x, y)
            time.sleep(time_delay_btw_clicks)

# Main program logic
if __name__ == "__main__":
    print("Press 'e' at any time to terminate the script.")  # Inform the user

    # Start the key listener thread
    start_key_listener()

    print("Timer mode? Press y/n (Y/N):")
    timer_mode = input().strip().lower() == 'y'

    if timer_mode:
        target_time = input("Enter start time (HH:MM:SS): ").strip()
    else:
        countdown_time = 10

    print("Spam mode? Press y/n (Y/N):")
    spam_mode = input().strip().lower() == 'y'

    num_clicks = int(input("How many spots do you want to click? ").strip())
    
    print("Do you want to capture new coordinates? (y/n):")
    if input().strip().lower() == 'y':
        coords = capture_coordinates(num_clicks)
    else:
        # Use default coordinates, slicing or repeating as needed.
        if len(default_coordinates) >= num_clicks:
            coords = default_coordinates[:num_clicks]
        else:
            # If not enough default coordinates, repeat the list until reaching the required count.
            times = (num_clicks // len(default_coordinates)) + 1
            coords = (default_coordinates * times)[:num_clicks]
    
    # Ask user if they want to refresh the page (simulate Ctrl+R) before waiting.
    print("Do you want to refresh the page (simulate Ctrl+R) before starting the timer/countdown? (y/n):")
    answer = input().strip().lower()
    
    # Wait based on timer mode.
    if timer_mode:
        wait_until(target_time)
    else:
        countdown_timer(countdown_time)
    
    if answer == 'y':
        refresh_page()
    time.sleep(0.1)  # wait for page to refresh
    # Start clicking
    click_spots(coords, spam_mode)

# use powershell as admin to open the file
# cd C:\Users\USERNAME\Desktop\"ders seçim"; python "auto clicker.py"
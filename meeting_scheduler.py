import schedule
import time
import subprocess
import pyautogui

def open_chrome_and_join(link):
    # Open Google Chrome
    subprocess.Popen(['C:\Program Files\Google\Chrome\Application\chrome.exe', link])
    
    # Wait for the browser to open and load the page (adjust the delay as needed)
    time.sleep(10)
    
    # Simulate clicking in the button "Join now" join the meeting (adjust the coordinates as needed)
    pyautogui.click(x=1268, y=595)

def demo_meeting():
    open_chrome_and_join('GOOGLE_MEET_LINK')  # Replace with your Google Meet URL

# Schedule the meeting for Tuesday to Friday at 8 AM
schedule.every().tuesday.at("08:00").do(demo_meeting)
schedule.every().wednesday.at("08:00").do(demo_meeting)
schedule.every().thursday.at("08:00").do(demo_meeting)
schedule.every().friday.at("08:00").do(demo_meeting)

while True:
    schedule.run_pending()
    time.sleep(1)

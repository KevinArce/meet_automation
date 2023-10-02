import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)

def demo_meeting():
    open_link('YOUR GOOGLE MEET LINK')  # Replace 'YOUR GOOGLE MEET LINK' with your Google Meet meeting URL

# Schedule the meeting for Tuesday to Friday at 8 AM
schedule.every().tuesday.at("08:00").do(demo_meeting)
schedule.every().wednesday.at("08:00").do(demo_meeting)
schedule.every().thursday.at("08:00").do(demo_meeting)
schedule.every().friday.at("08:00").do(demo_meeting)

while True:
    schedule.run_pending()
    time.sleep(1)

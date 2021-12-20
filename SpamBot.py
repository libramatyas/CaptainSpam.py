import pyautogui
import webbrowser
import time

message = input("Message To Spam! Leave Blank if you want to spam your clipboard")
repeat = int(input(("How Many Times To Send This Message!")))
delay = int(input("How Many Milliseconds in between every message!"))

isLoaded = input("press enter when your discord is loaded")


print("You Have 5 seconds before spam starts")

time.sleep(5)

for i in range (0,repeat):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press('enter')
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    
    time.sleep(delay/1000)

print("Done\n")
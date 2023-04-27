from plyer import notification
import time

if __name__ =='__main__':
    while True:
        notification.notify(
            title="***take rest***",
            message="Improve mood and better experience take rest: by_Manish",
            timeout=5)
        time.sleep(2) #sleeping time 

#pythonw file.py
import watchdog.observers
import watchdog.events
import os
import sys
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyOrganizer(FileSystemEventHandler):
    print("Organizer is created!")

    def on_created(self,event):

        for filename in os.listdir(folder):
            src = folder + "/" + filename
            fn, file_type = os.path.splitext(src)
            new_dst = folder_dst + "/" + file_type

            # check if file type folder exists
            if not os.path.exists(new_dst):
                # if it does NOT exist, create the file type folder
                print("MAKING NEW " + file_type + " FOLDER !")
                os.mkdir(new_dst)
            
            new_dst = new_dst  + "/" + filename
            os.rename(src, new_dst)
            print(filename + " was moved to " + new_dst + " !")


# location of folder and where files will go
folder = "/Users/Jason/Downloads"
folder_dst = "/Users/Jason/Downloads"


handler = MyOrganizer()
observer = Observer()

observer.schedule(handler, folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
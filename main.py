import os
import time

# replace with your Downloads folder path
folder_path = "/path/to/Downloads/folder"

# replace with the number of days to keep files
days_threshold = 30

while True:
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.stat(file_path).st_mtime < time.time() - days_threshold * 86400:
            os.remove(file_path)

    # Wait 5 minutes before checking again
    time.sleep(300)
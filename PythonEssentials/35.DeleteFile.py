import os
import shutil

path = "C:\\Users\\WONDERS\\Documents\\SampleTes.txt"

try:
    os.remove(path) # delete file
    #os.rmdir(path)  # delete an empty directory
    #shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do no have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")

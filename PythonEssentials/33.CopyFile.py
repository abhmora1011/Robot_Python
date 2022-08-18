# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('C:\\Users\\WONDERS\\Documents\\SampleTest.txt', 'C:\\Users\\WONDERS\\Documents\\copy.txt') # src, dst
shutil.copy('C:\\Users\\WONDERS\\Documents\\SampleTest.txt', 'C:\\Users\\WONDERS\\Documents\\copy2.txt') # src, dst
shutil.copy2('C:\\Users\\WONDERS\\Documents\\SampleTest.txt', 'C:\\Users\\WONDERS\\Documents\\copy3.txt') # src, dst
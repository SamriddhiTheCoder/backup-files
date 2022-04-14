import time
import shutil
import os

path = input("Enter a path: ")
days = 1095

days = time.time()

if (os.path.exists(path)):
    for dic, files in path:
        files_list = os.walk(path)
    new_path = os.path.join(path, files_list)
    ctime = os.stat(path).st_ctime

    if (ctime > days):
        os.remove(new_path)
        shutil.rmtree()

else: 
    print("Path not found!")
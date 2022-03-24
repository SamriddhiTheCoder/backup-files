import time
import shutil
import os

path = input("Enter a path: ")
days = 500

days = time.time()

if (os.path.exists(path)):
    os.walk(path)
    os.path.join(path)
    ctime = os.stat(path).st_ctime

    if (ctime > days):
        os.remove(path)
        shutil.rmtree()

else: 
    print("Path not found!")
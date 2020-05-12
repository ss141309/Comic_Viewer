import os
import glob

def mkdirs(dir):

    os.makedirs(dir, exist_ok = True) # exist_ok: if the folder already exists it will not throw an error


def cleanup(dir): # https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
    mypath = os.path.join(dir, '*.jpg')
    files = glob.glob(mypath)
    for f in files:
        os.remove(f)

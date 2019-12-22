import os
import shutil

folders = {
    "m4a": "m4a_files//", 
    "wav": "wav_files//", 
    "txt": "txt_files//"
}

extensions = {
    "m4a": ".m4a", 
    "wav": ".wav", 
    "txt": ".txt"
}

def create_filename(name, type):
    return folders[type] + name + extensions[type]

def make_folder(folder):
    try: 
        os.mkdir(folder) 
    except(FileExistsError): 
        pass

def remove_folder(folder):
    try:
        shutil.rmtree(folder)
    except(FileExistsError): 
        pass


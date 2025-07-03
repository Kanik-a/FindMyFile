import os
from rapidfuzz import process, fuzz, utils
def process_text(text):
    print(f"Processing {text}")
    print(len(text), text.lower())
    list_of_files = fileData()
    fileSeek = searchFile(text, list_of_files)
    file_to_open = openFile(fileSeek)
    return fileSeek
    
def fileData():
    folder_path = "C:/Users/kanik/OneDrive/Desktop"
    filesFolders = os.listdir(folder_path)
    return filesFolders
     
    
    
def searchFile(text, fileFolders):
    processing = process.extract(text, fileFolders, scorer=fuzz.WRatio, limit=3, processor=utils.default_process)
    res = f"Best Matches: {processing}"
    user_file = []
    for x in processing:
        user_file.append(x[0])
        
    return user_file

def openFile(user_file):
    for x in user_file:
        os.startfile(x)
    
    



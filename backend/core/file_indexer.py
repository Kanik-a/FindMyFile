import os, re
from rapidfuzz import process, fuzz, utils
def process_text(text):
    print(f"Processing {text}")
    print(len(text), text.lower())
    list_of_files = fileData()
    fileSeek = searchFile(text, list_of_files)
    preprocessFile = preprocessFileNames(fileSeek)
    #file_to_open = openFile(fileSeek)
    return fileSeek, preprocessFile
    
def fileData():
    folder_path = "C:/Users/kanik/OneDrive/Desktop/Documents and Headshots"
    filesFolders = os.listdir(folder_path)
    return filesFolders
     
def searchFile(text, fileFolders):
    processing = process.extract(text, fileFolders, scorer=fuzz.ratio, limit=3, processor=utils.default_process)
    user_file = []
    for x in processing:
        user_file.append(x[0])
    return user_file
    
def preprocessFileNames(user_file):
    processed_file_names = []
    for filename in user_file:
        if not filename:
            return ""
        filename = re.sub(r"[_\-.,:;!?()]+", " ", filename)
        filename = re.sub(r"\s+", " ", filename)
        filename = filename.lower()
        processed_file_names.append(filename)
    return processed_file_names
        
def openFile(user_file):
    for x in user_file:
        os.startfile(x)
    
    



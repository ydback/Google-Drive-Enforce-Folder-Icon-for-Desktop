import os

# Folder delimiter: /
def folderString(*FolderStr):
    first = FolderStr[0]
    if first[-1] != '/':
        first += '/'
    for i in range(1, len(FolderStr)):
        middle = FolderStr[i]
        if middle[-1] != '/':
            middle += '/'
        if middle[0] == '/':
            middle = middle[1:]
        first += middle
    return first


TOKEN_FOLDER_ICON = "FOLDER_ICON"
TOKEN_FOLDER_GOOGLE_DRIVE = "FOLDER_GOOGLE_DRIVE"


FILENAME_FOLDER_INI = "folder.ini"
def read_ini_file(filename):
    data = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                data[key.strip()] = value.strip()
    return data


def updateINI():
    folderINI = read_ini_file(FILENAME_FOLDER_INI)
    f_icos = open("icos.txt", encoding="utf-8")
    count_success = 0
    count_fail = 0
    for line in f_icos:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        folder, icoFolder, icoFile = list(map(lambda x: x.strip(), line.split(",")))
         
        ffolder = folderString(folderINI[TOKEN_FOLDER_GOOGLE_DRIVE], folder)
        fname = ffolder + "Desktop.ini"
        if os.path.exists(ffolder):
            os.chdir(ffolder)
            if os.path.exists("Desktop.ini"):
                os.system('attrib -h -s Desktop.ini')
            f = open("Desktop.ini", "w")
            f.write("[.ShellClassInfo]" + '\n')
            f.write("IconFile=" + folderString(folderINI[TOKEN_FOLDER_ICON], icoFolder) + icoFile + '\n')
            f.write("IconIndex=0")
            f.close()
            os.system('attrib +h +s Desktop.ini')
            count_success += 1
        else:
            print("Path " + ffolder + " not found.")
    print(str(count_success) + " custom folder icons applied, " + str(count_fail) + " failed.")
    f_icos.close()
    

updateINI()

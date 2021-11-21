import os

# Folder that installed FolderPainter
FOLDER_FOLDER_PAINTER_ICON = "C:/Program Files/FolderPainter/Icons/"
FOLDER_GOOGLE_DRIVE = "C:/Users/daich/Google Drive/"

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


def updateINI():
    f_icos = open("icos.txt", "r")
    for ico in f_icos:
        print(ico)
        folder, icoFolder, icoFile = ico.split(",")
         
        ffolder = folderString(FOLDER_GOOGLE_DRIVE, folder)
        fname = ffolder + "Desktop.ini"
        os.chdir(ffolder)
        if os.path.exists(fname):
            os.system('attrib -h -s Desktop.ini')
        f = open(fname, "w")
        f.write("[.ShellClassInfo]" + '\n')
        f.write("IconFile=" + folderString(FOLDER_FOLDER_PAINTER_ICON, icoFolder) + icoFile + '\n')
        f.write("IconIndex=0")
        f.close()
        os.system('attrib +h +s Desktop.ini')
    f_icos.close()


updateINI()
input()
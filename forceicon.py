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


FOLDER_TOKENS = ["FOLDER_ICON", "FOLDER_GOOGLE_DRIVE"]
TOKEN_FOLDER_ICON = 0
TOKEN_FOLDER_GOOGLE_DRIVE = 1

def readFolderINI():
    folderINI = [""] * len(FOLDER_TOKENS)
    f = open("folder.ini", "r")
    for lineRaw in f:
        line = processFileLine(lineRaw)
        if len(line) == 0:
            continue
        line = line.split("=")
        tokenInd = FOLDER_TOKENS.index(line[0])
        if tokenInd >= 0:
            folderINI[tokenInd] = line[1]
    f.close()
    return folderINI


def updateINI():
    folderINI = readFolderINI()
    f_icos = open("icos.txt", "r")
    count = 0
    for icoRaw in f_icos:
        ico = processFileLine(icoRaw)
        if len(ico) == 0:
            continue
        folder, icoFolder, icoFile = ico.split(",")
         
        ffolder = folderString(folderINI[TOKEN_FOLDER_GOOGLE_DRIVE], folder)
        fname = ffolder + "Desktop.ini"
        os.chdir(ffolder)
        if os.path.exists(fname):
            os.system('attrib -h -s Desktop.ini')
        f = open(fname, "w")
        f.write("[.ShellClassInfo]" + '\n')
        f.write("IconFile=" + folderString(folderINI[TOKEN_FOLDER_ICON], icoFolder) + icoFile + '\n')
        f.write("IconIndex=0")
        f.close()
        os.system('attrib +h +s Desktop.ini')
        count += 1
    print(str(count) + " custom folder icons applied.")
    f_icos.close()


def processFileLine(lineRaw):
    line = lineRaw.strip()
    if len(line) == 0:
        return ""
    line = line.split("#")[0]
    line = line.split("%")[0]
    return line
    

updateINI()
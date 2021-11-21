# So Google Drive resets your folder icons again? Maintain a list of folder icons from now on.

This is intended to record the custom folder icon you are using for any folders in Google Drive, as by now Google Drive now reverts all folder icon changes from time to time.

## Setup

#### Modify forceicon.py:
FOLDER_FOLDER_PAINTER_ICON: The root directory of your own folder icons. I myself uses Folder Painter's icons, but you can use any folder icons.
FOLDER_GOOGLE_DRIVE: The root directory of your google drive folder.

#### Create/Edit icos.txt in the same folder:
For each folder you want to customize the icon, write:
- Relative path of folder of the folder you want to customize, from Google Drive root directory
- Relative path of folder of the desired icon
- File name of the desired icon

Delimited by ",".

Example:
```
Course Notes,Pack_01,01.ico
Doctor/Plan,Pack_01,04.ico
```

## Run forceicon.py

From now on, whenever you want to customize a folder in google drive, edit icos.txt and run forceicon.py.

Whenever Google Drive messed up your folder icons again, run forceicon.py.

*Modify as you wish, and run with risk.*

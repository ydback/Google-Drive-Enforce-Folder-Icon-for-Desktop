# So Google Drive resets your folder icons again? Maintain a list of folder icons from now on.

This is intended to record the custom folder icon you are using for any folders in Google Drive, as by now Google Drive now reverts all folder icon changes from time to time.

## Setup

#### Create/Edit folder.ini as below:
```
FOLDER_ICON=C:/Program Files/FolderPainter/Icons/
FOLDER_GOOGLE_DRIVE=C:/Users/myusername/Google Drive/
```

#### Then edit:

- `FOLDER_ICON`: The root directory of your own folder icons. You can leave it empty/remove this token and always use absolute paths in icos.txt instead.
- `FOLDER_GOOGLE_DRIVE`: The root directory of your google drive folder.

#### Create/Edit icos.txt in the same folder:
For each folder you want to customize the icon, write:
- Relative path of folder of the folder you want to customize, from Google Drive root directory
- Relative path of folder of the desired icon
- File name of the desired icon

in one line, delimited by `,`.

Leading and trailing spaces are ignored.<br />
Contents after `#` or `%` in a line are ignored.<br />
Empty lines are ignored.<br />

Example:
```
Course Notes,Pack_01,01.ico

# My Doctor projects:
Doctor,Pack_01,04.ico
Doctor/Project,Pack_01,03.ico # Coloured as green for having outstanding items
Doctor/Plan,Pack_01,04.ico
```

## Run forceicon.py

From now on, whenever you want to customize a folder in google drive, edit icos.txt and run forceicon.py.

Whenever Google Drive messed up your folder icons again, run forceicon.py.

*Modify as you wish, and run with risk.*

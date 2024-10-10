# folder-organization
Python script to organize a folder


This small project of mine will help you sort through all your files in a single directory.
Please note that this program does not sort through sub-folders. You only need python to run this program.
It uses a file directory broswer to pick a folder. Once you pick the folder/directory you wish to sort through,
It will run the code twice.

The first time sorts the files into its own folder with the same name as the file extension.
If the file is a folder/directory, it will sort it into its own folder called 'folder'. If for some reason you already
have a folder called 'folder', it will just add the folders into there.

The second time it runs, it takes all those folders that it created and places them into the 'folder' folder.

Once the program is finished, all that should remain is a single folder named 'folder'.
If you have any files that don't have an extension name, they will be ignored.
If you have any program shortcuts, they will also remain there. This includes desktop shortcuts as well.

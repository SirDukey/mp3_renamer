# ----------------------------------------------------------
# Date: 27-11-2017
# Author: Mike Duke
#
# Rename mp3 files that look like artist - album - title.mp3
# to artist - title.mp3
#
# ----------------------------------------------------------

# os library is used to show directories, list files, delete files
import os
# shutil is a library for shell utilites, it can perform a file rename, similar to linux mv command
import shutil

# Change to the directory where the MP3 files are
os.chdir('/home/mike/Music/Pat Metheny - Unity Band (2012)')

# If there is a ReadMe.txt file in the directory delete it

if 'ReadMe.txt' in os.listdir():
    # unlink deletes the file
    os.unlink('ReadMe.txt')
    print('Removed: ReadMe.txt')

# get a list of the files in the directory and call it `album`
album = os.listdir()


# this is just in case you want to print the files to the screen
def old_name():
    for song in album:
        print(song)


# going to rename the files now
def new_name():

    for song in album:
        # go through each song in the album list and split it at every `-`
        # eg, the song would originally look like this `artist - album - title.mp3`
        split_list = song.split('-')
        # remove some blank space on the song name
        strip_list = [x.strip(' ') for x in split_list]
        # 
        for item in strip_list:
            # make a new track name `artis - title.mp3`
            new_track_name = (" - ".join(strip_list[0:2]) + '.mp3')
        
        # rename the original file to the new file name
        shutil.move(song, new_track_name)
        print('Renamed: %s to %s' % (song, new_track_name))

        
# run the functions if the file is run from the command line
if __name__ == "__main__":
    new_name()

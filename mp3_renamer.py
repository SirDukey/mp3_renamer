# --------------------------------------------------------
# Date: 27-11-2017
# Author: Mike Duke
#
# Rename mp3 files
#
# --------------------------------------------------------


import os
import shutil

os.chdir('/home/mike/Music/Pat Metheny - Unity Band (2012)')

if 'ReadMe.txt' in os.listdir():
    os.unlink('ReadMe.txt')
    print('Removed: ReadMe.txt')

album = os.listdir()




def old_name():
    for song in album:
        print(song)


def new_name():

    for song in album:
        split_list = song.split('-')
        strip_list = [x.strip(' ') for x in split_list]

        for item in strip_list:
            new_track_name = (" - ".join(strip_list[0:2]) + '.mp3')

        shutil.move(song, new_track_name)
        print('Renamed: %s to %s' % (song, new_track_name))

new_name()

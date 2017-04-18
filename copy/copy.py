# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys

def copy():
    controller = sys.argv[1:]
    if len(controller) == 1 and controller[0]== 'cp':
        print('copy [source] [destination]')
    elif len(controller) == 2:
        print('No destination provided')
    elif len(controller) == 3:
        try:
            read()
        except FileNotFoundError:
            print('One or both of your files are not found')
#
def read():
    controller = sys.argv[1:]
    file_1 = str(controller[1])
    source = open(file_1,'r')
    source = source.read()

    controller = sys.argv[1:]
    file_2 = str(controller[2])
    dest = open(file_2,'a')
    dest.write(source)

copy()
#read_write()

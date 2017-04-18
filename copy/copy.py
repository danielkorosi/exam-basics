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

copy()

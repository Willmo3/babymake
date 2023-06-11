#!/usr/bin/env python3

from sys import argv
from os import getcwd
from os.path import isfile

ARG_LEN = 3
LANG_INDEX = 1
TARGET_INDEX = 2

EXIT_SUCCESS = 0
EXIT_FAILURE = 1 

def main():
    if len(argv) != ARG_LEN:
        print("Usage: python bm.py [language] [name]")
        return EXIT_FAILURE

    comp = None           # Compiler to use.
    src = None            # Program source file.
    ext = None            # extension for source file.
    target = None         # Name of output file.

    lang = argv[LANG_INDEX]
    if lang.lower() == "c":
        comp = "gcc"
        ext = ".c"
    elif lang.lower() == "cpp":
        comp = "g++"
        ext = ".cpp"
    else:
        print("Invalid language: " + lang + ". Options are: c, cpp")
        return EXIT_FAILURE

    target = argv[TARGET_INDEX]
    src = "{}{}".format(argv[TARGET_INDEX], ext)

    if not isfile(src):
        print("Invalid source file (does it exist?): " + src)
        return EXIT_FAILURE
    
    path = getcwd() + "/makefile"
    # Prevent accidental deletions. 
    if isfile(path):
        print("Warning! Makefile found at: " + path + ". Remove this from path before continuing!")
        return EXIT_FAILURE
    
    with open(path, "w") as makefile:
        message = f'CC = {comp}\n'
        message += f'EXT = {ext}\n'
        message += 'CFLAGS = -Wall\n\n'
        message += f'TARGET = {target}\n\n'
        message += '$(TARGET):$(TARGET)$(EXT)\n'
        message += '\t$(CC) $(CFLAGS) -o $(TARGET) $(TARGET)$(EXT)\n\n'
        message += 'clean:\n'
        message += '\t$(RM) $(TARGET)\n'
        
        makefile.write(message)
    
    return EXIT_SUCCESS

if __name__ == "__main__":
    main()

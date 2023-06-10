Babymake: baby's first make file!

Explanation:
I made this script when I was learning C++ because I was tired of having to write a makefile for every toy program I made.

Babymake creates a small makefile which compiles a single file in either C or C++ to an output binary with the same name as the input file, minus the extension. 

The makefile made by Babymake is decently modular, and so can be a baseline for larger programs.

Usage:
python bm.py [language] [name] 

Where language is "c" or "cpp" and name is the name of the output binary, AND ALSO the name of the src file minus the extension.
E.G. python bm.py c hello : build a makefile for compiling hello.c into hello.

Example makefile:

CC = gcc
EXT = .c
CFLAGS = -Wall

TARGET = hello

$(TARGET):
        $(CC) $(CFLAGS) -o $(TARGET) $(TARGET)$(EXT)

clean:
        $(RM) $(TARGET)

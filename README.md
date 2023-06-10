# Babymake  
Baby's first make file!

## Explanation:  
I made this script when I was learning C++ because I was tired of having to write a makefile for every toy program I made.  

Babymake creates a small makefile which compiles a single file in either C or C++ to an output binary with the same name as the input file, minus the extension. 

Note: I've chosen not to allow specifying the output name as different from the input for simplicity and ease of use. 
  
The makefile made by Babymake is decently modular, and so can be a baseline for larger programs.  
  
## Usage:  
python bm.py [language] [name]  
  
Where language is "c" or "cpp" and name is the name of the output binary, AND ALSO the name of the source file minus the extension.

### Examples:
`python bm.py c hello` : build a makefile for compiling hello.c into output binary hello.

`python bm.py cpp test` : build a makefile for compiling test.cpp into output binary test.

## Example Makefile:  

CC = gcc  
EXT = .c  
CFLAGS = -Wall  
 
TARGET = hello  

\$(TARGET):  
    \$(CC) \$(CFLAGS) -o \$(TARGET) \$(TARGET)\$(EXT)  
  
clean:  
    \$(RM) \$(TARGET)

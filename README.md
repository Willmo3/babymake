# Babymake  
Baby's first make file!  
  
## Explanation:  
I made this script when I was learning C++ because I was tired of having to write a makefile for every toy program I made.  
  
Babymake creates a small makefile which compiles a single file in either C or C++ to an output binary with the same name as the input file, minus the extension.  
  
The makefile made by Babymake is decently modular, and so can be a baseline for larger programs.  

## Dependencies:

 - Python 3 
	 - I used version 3.10.6. It shouldn't matter.
 - Make
 - The respective compiler for your language (gcc/g++)

For simplicity, consider installing the [build-essential](https://packages.debian.org/sid/build-essential) package (or your distro's equivalent), which will contain make, gcc, g++, and other useful goodies. 

 - Debian: `apt install build-essential`
 - RedHat: `dnf groupinstall "Development Tools" "Development Libraries"`
 - Arch: `pacman -Sy base-devel`
  
## Usage:  
`python bm.py [language] [name]` 
OR `./bm.py [language] [name]` if marked as executable.
  
Where language is "c" or "cpp" and name is the name of the output binary, AND ALSO the name of the source file minus the extension.  
  
### Examples:  
`./bm.py c hello` : build a makefile for compiling hello.c into output binary hello.  
  
`./bm.py cpp test` : build a makefile for compiling test.cpp into output binary test.  
  
## Example Makefile:  
  
CC = gcc  
EXT = .c  
CFLAGS = -Wall  
  
TARGET = hello  
  
\$(TARGET):  
&nbsp;&nbsp;&nbsp;&nbsp;\$(CC) \$(CFLAGS) -o \$(TARGET) \$(TARGET)\$(EXT)  
  
clean:  
&nbsp;&nbsp;&nbsp;&nbsp;\$(RM) \$(TARGET)


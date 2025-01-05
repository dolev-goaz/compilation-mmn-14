@echo off

:: configurations
set CC=gcc
set CFLAGS=-Wall -g
set OBJDIR=obj
set LEX=win_flex
set YACC=win_bison

:: output file
set TARGET=list
set OBJS=%OBJDIR%\my_list.o %OBJDIR%\list.tab.o %OBJDIR%\lla.yy.o

:: create object directory if it doesn't exist
if not exist %OBJDIR% mkdir %OBJDIR%

:: compile list.c
%CC% -c my_list.c %CFLAGS% -o %OBJDIR%\my_list.o

:: generate the parser source code
%YACC% -d list.y

:: compile the parser source code
%CC% -c list.tab.c %CFLAGS% -o %OBJDIR%\list.tab.o

:: generate the lexer source code
%LEX% -o lla.yy.c lla.lex

:: compile the lexer source code
%CC% -c lla.yy.c %CFLAGS% -o %OBJDIR%\lla.yy.o

:: compile final executable
%CC% -o %TARGET% %OBJS%


:: cleanup
rmdir /s /q %OBJDIR%
del /q *.tab.c *.tab.h *.yy.c

echo Build complete.
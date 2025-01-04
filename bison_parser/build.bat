@echo off
win_bison -v -d list.y &:: add -t for debugging
win_flex lla.lex &:: list lexical analyzer
gcc lex.yy.c list.tab.c
win_bison -v list.y
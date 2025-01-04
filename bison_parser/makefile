# configurations
CC = gcc
CFLAGS = -Wall -g
LEX = flex
YACC = bison
LEXER = lla
PARSER = list
OBJDIR = obj

# output file
TARGET = parser

# source files
SRCS = list.c list.y lla.lex
OBJS = $(OBJDIR)/list.o $(OBJDIR)/list.tab.o $(OBJDIR)/lla.yy.o

# compile final executable
$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

# compile list.c
$(OBJDIR)/list.o: list.c list.h | $(OBJDIR)
	$(CC) -c list.c $(CFLAGS) -o $(OBJDIR)/list.o

# generate and compile the parser source code
$(OBJDIR)/list.tab.c $(OBJDIR)/list.tab.h: list.y | $(OBJDIR)
	$(YACC) -d list.y
	mv list.tab.c $(OBJDIR)/list.tab.c
	mv list.tab.h $(OBJDIR)/list.tab.h

# generate the lexer source code
$(OBJDIR)/lla.yy.c: lla.lex | $(OBJDIR)
	$(LEX) -o $(OBJDIR)/lla.yy.c lla.lex

# compile the lexer source code
$(OBJDIR)/lla.yy.o: $(OBJDIR)/lla.yy.c | $(OBJDIR)
	$(CC) -c $(OBJDIR)/lla.yy.c $(CFLAGS) -o $(OBJDIR)/lla.yy.o

# create object directory if it doesn't exist
$(OBJDIR):
	mkdir -p $(OBJDIR)


clean:
	rm -rf $(OBJDIR) $(TARGET)


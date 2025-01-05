# configurations
CC = gcc
CFLAGS = -Wall -g
OBJDIR = obj
LEX = flex
YACC = bison

# output file
TARGET = list
OBJS = $(OBJDIR)/my_list.o $(OBJDIR)/list.tab.o $(OBJDIR)/lla.yy.o

# compile final executable
$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

# compile list.c
$(OBJDIR)/my_list.o: my_list.c my_list.h | $(OBJDIR)
	$(CC) -c my_list.c $(CFLAGS) -o $(OBJDIR)/my_list.o

# generate the parser source code
list.tab.c list.tab.h: list.y
	$(YACC) -d list.y

# compile the parser source code
$(OBJDIR)/list.tab.o: list.tab.c list.tab.h | $(OBJDIR)
	$(CC) -c list.tab.c $(CFLAGS) -o $(OBJDIR)/list.tab.o

# generate the lexer source code
lla.yy.c: lla.lex
	$(LEX) -o lla.yy.c lla.lex

# compile the lexer source code
$(OBJDIR)/lla.yy.o: lla.yy.c | $(OBJDIR)
	$(CC) -c lla.yy.c $(CFLAGS) -o $(OBJDIR)/lla.yy.o

# create object directory if it doesn't exist
$(OBJDIR):
	mkdir -p $(OBJDIR)

clean:
	rm -rf $(OBJDIR) $(TARGET)
	rm -f list.tab.c list.tab.h lla.yy.c


# configurations
CC = gcc
CFLAGS = -Wall -g
OBJDIR = obj
YACC = bison

# output file
TARGET = parser
OBJS = $(OBJDIR)/list.o $(OBJDIR)/list.tab.o $(OBJDIR)/lla.yy.o

# compile final executable
$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

# compile list.c
$(OBJDIR)/list.o: list.c list.h | $(OBJDIR)
	@echo "Compiling list.c..."
	$(CC) -c list.c $(CFLAGS) -o $(OBJDIR)/list.o

# generate the parser source code
list.tab.c list.tab.h: list.y
	@echo "Generating parser source code"
	$(YACC) -d list.y

# compile the parser source code
$(OBJDIR)/list.tab.o: list.tab.c list.tab.h | $(OBJDIR)
	@echo "Compiling parser source code"
	$(CC) -c list.tab.c $(CFLAGS) -o $(OBJDIR)/list.tab.o

# generate the lexer source code
lla.yy.c: lla.lex
	@echo "Generating lexer source code"
	$(LEX) -o lla.yy.c lla.lex

# compile the lexer source code
$(OBJDIR)/lla.yy.o: lla.yy.c | $(OBJDIR)
	@echo "Compiling lexer source code"
	$(CC) -c lla.yy.c $(CFLAGS) -o $(OBJDIR)/lla.yy.o

# create object directory if it doesn't exist
$(OBJDIR):
	@echo "Creating obj directory..."
	mkdir -p $(OBJDIR)

clean:
	rm -rf $(OBJDIR) $(TARGET)
	rm -f list.tab.c list.tab.h lla.yy.c


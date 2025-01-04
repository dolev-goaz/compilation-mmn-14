%code {
    #include <stdio.h>
    extern int yylex(void);
    void yyerror(const char* s);
}

%union {
    int val;
    char list; // TODO: add list type
}


/* expressions and types */
%token <val> NUMBER

%token '(' ')' '[' ']' ','
%token TAIL APPEND DIVIDE
%token SUM EQUAL


%nterm S
%nterm <val> ITEM
%nterm <list> L ITEMLIST

/* doesnt work for some reason, probably need newer bison version? */
/* %define parser.error verbose */

%start S

%% /* grammar */

S:
    NUMBER { printf("%d\n", $1); }
    ;
%%

int main(int argc, char** argv) {
    return 0;
}

void yyerror(char const *s) {
   fprintf(stderr, "%s\n", s);
}
%code {
    #include <stdio.h>
    #include "my_list.h"
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
/* used 'type' instead of 'nterm' because of the language server i use */
%type <val> item
%type <list> L itemlist

/* doesnt work for some reason, probably need newer bison version? */
/* %define parser.error verbose */

%start S

%% /* grammar */

S:
    item                        { printf("%d\n", $1); }
    ;

L:
    '[' itemlist ']'            { $$ = '\0'; }
    | TAIL '(' L ')'            { $$ = '\0'; }
    | APPEND '(' item ',' L ')' { $$ = '\0'; }
    | DIVIDE '(' item ',' L ')' { $$ = '\0'; }

itemlist:
    itemlist ',' item           { $$ = '\0'; }
    | item                      { $$ = '\0'; }

item:
    SUM '(' L ')'               { $$ = 0;  }
    | EQUAL '(' L ')'           { $$ = 0;  }
    | NUMBER                    { $$ = $1; }
    ;

%%

int main(int argc, char** argv) {
    extern FILE *yyin;
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input-file-name>\n", argv[0]);
        return 1;
    }
    yyin = fopen(argv[1], "r");
    if (!yyin) {
        fprintf(stderr, "Error while opening file '%s'\n", argv[1]);
        return 2;
    }
    yyparse();

    fclose(yyin);
    return 0;
}

void yyerror(char const *s) {
   fprintf(stderr, "%s\n", s);
}
%{
#include <stdlib.h>
#include "list.tab.h"
%}

%option noyywrap

%%
 /* keywords */
tail    { return TAIL;   }
append  { return APPEND; }
divide  { return DIVIDE; }
sum     { return SUM;    }
equal   { return EQUAL;  }

[0-9]+ { yylval.val = atoi(yytext); return NUMBER; }

 /* symbols */
\( { return '('; }
\) { return ')'; }
\[ { return '['; }
\] { return ']'; }
,  { return ','; }

. { fprintf(stderr, "Error: Unknown token: '%s'", yytext); }
							   
%%
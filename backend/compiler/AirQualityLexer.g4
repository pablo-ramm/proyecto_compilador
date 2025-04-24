lexer grammar AirQualityLexer;

// Keywords and identifiers
DATE        : [0-9][0-9][0-9][0-9] '-' [0-9][0-9] '-' [0-9][0-9] ;
TIME        : [0-9][0-9] ':' [0-9][0-9] (':' [0-9][0-9])? ;
FLOAT       : '-'? [0-9]+ '.' [0-9]+ ;
INTEGER     : '-'? [0-9]+ ;
IDENTIFIER  : [a-zA-Z][a-zA-Z0-9_]* ;
STRING      : '"' .*? '"' | '\'' .*? '\'' ;

// Units
PPM         : 'ppm' | 'PPM' ;
PPB         : 'ppb' | 'PPB' ;
UGM3        : 'µg/m³' | 'ug/m3' | 'µg/m3' | 'ug/m³' ;
PERCENT     : '%' ;

// Pollutants
PM25        : 'PM2.5' | 'pm2.5' | 'PM2_5' | 'pm2_5' ;
PM10        : 'PM10' | 'pm10' ;
O3          : 'O3' | 'o3' | 'ozone' | 'OZONE' ;
NO2         : 'NO2' | 'no2' | 'nitrogen dioxide' | 'NITROGEN DIOXIDE' ;
SO2         : 'SO2' | 'so2' | 'sulfur dioxide' | 'SULFUR DIOXIDE' ;
CO          : 'CO' | 'co' | 'carbon monoxide' | 'CARBON MONOXIDE' ;

// Symbols
COMMA       : ',' ;
SEMICOLON   : ';' ;
COLON       : ':' ;
DOT         : '.' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
LBRACK      : '[' ;
RBRACK      : ']' ;
PLUS        : '+' ;
MINUS       : '-' ;
STAR        : '*' ;
SLASH       : '/' ;
EQUAL       : '=' ;
NOTEQUAL    : '!=' ;
GT          : '>' ;
LT          : '<' ;
GE          : '>=' ;
LE          : '<=' ;

// Quality categories
GOOD        : 'Good' | 'GOOD' | 'good' ;
MODERATE    : 'Moderate' | 'MODERATE' | 'moderate' ;
UNHEALTHY   : 'Unhealthy' | 'UNHEALTHY' | 'unhealthy' ;
HAZARDOUS   : 'Hazardous' | 'HAZARDOUS' | 'hazardous' ;

// Whitespace and comments
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
'''

# File: AirQualityParser.g4
'''
parser grammar AirQualityParser;

options { tokenVocab=AirQualityLexer; }

// Main parsing rule
airQualityData : record+ EOF ;

// A record can be in different formats
record : standardRecord | jsonRecord | csvRecord ;

// Standard record format
standardRecord : date time? measurements ;

// JSON-like record
jsonRecord : LBRACE jsonField (COMMA jsonField)* RBRACE ;
jsonField : IDENTIFIER COLON (STRING | FLOAT | INTEGER | jsonRecord | LBRACK jsonRecord (COMMA jsonRecord)* RBRACK) ;

// CSV-like record
csvRecord : field (COMMA field)* ;
field : (STRING | FLOAT | INTEGER | IDENTIFIER | date | time) ;

// Date and time
date : DATE ;
time : TIME ;

// Measurements of pollutants
measurements : measurement (SEMICOLON measurement)* ;
measurement : pollutant value unit? quality? ;

// Pollutant types
pollutant : PM25 | PM10 | O3 | NO2 | SO2 | CO | IDENTIFIER ;

// Value can be numeric
value : FLOAT | INTEGER ;

// Units of measurement
unit : PPM | PPB | UGM3 | PERCENT ;

// Air quality category
quality : GOOD | MODERATE | UNHEALTHY | HAZARDOUS ;
'''

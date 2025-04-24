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

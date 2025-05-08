# Generated from AirQualityParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,1,1,1,1,1,3,1,41,
        8,1,1,2,1,2,3,2,45,8,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,
        3,56,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,70,
        8,4,10,4,12,4,73,9,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,5,5,82,8,5,10,
        5,12,5,85,9,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,93,8,6,1,7,1,7,1,8,1,8,
        1,9,1,9,1,9,5,9,102,8,9,10,9,12,9,105,9,9,1,10,1,10,1,10,3,10,110,
        8,10,1,10,3,10,113,8,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,
        1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,4,2,0,5,5,
        11,16,1,0,3,4,1,0,7,10,1,0,37,40,126,0,31,1,0,0,0,2,40,1,0,0,0,4,
        42,1,0,0,0,6,48,1,0,0,0,8,59,1,0,0,0,10,78,1,0,0,0,12,92,1,0,0,0,
        14,94,1,0,0,0,16,96,1,0,0,0,18,98,1,0,0,0,20,106,1,0,0,0,22,114,
        1,0,0,0,24,116,1,0,0,0,26,118,1,0,0,0,28,120,1,0,0,0,30,32,3,2,1,
        0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,
        1,0,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,41,3,4,2,0,38,41,3,6,3,0,39,
        41,3,10,5,0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,
        0,42,44,3,14,7,0,43,45,3,16,8,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,
        1,0,0,0,46,47,3,18,9,0,47,5,1,0,0,0,48,49,5,23,0,0,49,54,3,8,4,0,
        50,51,5,17,0,0,51,53,3,8,4,0,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,
        0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,58,5,24,0,0,58,
        7,1,0,0,0,59,60,5,5,0,0,60,76,5,19,0,0,61,77,5,6,0,0,62,77,5,3,0,
        0,63,77,5,4,0,0,64,77,3,6,3,0,65,66,5,25,0,0,66,71,3,6,3,0,67,68,
        5,17,0,0,68,70,3,6,3,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,26,0,0,75,77,1,
        0,0,0,76,61,1,0,0,0,76,62,1,0,0,0,76,63,1,0,0,0,76,64,1,0,0,0,76,
        65,1,0,0,0,77,9,1,0,0,0,78,83,3,12,6,0,79,80,5,17,0,0,80,82,3,12,
        6,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,11,
        1,0,0,0,85,83,1,0,0,0,86,93,5,6,0,0,87,93,5,3,0,0,88,93,5,4,0,0,
        89,93,5,5,0,0,90,93,3,14,7,0,91,93,3,16,8,0,92,86,1,0,0,0,92,87,
        1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,
        93,13,1,0,0,0,94,95,5,1,0,0,95,15,1,0,0,0,96,97,5,2,0,0,97,17,1,
        0,0,0,98,103,3,20,10,0,99,100,5,18,0,0,100,102,3,20,10,0,101,99,
        1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,19,1,
        0,0,0,105,103,1,0,0,0,106,107,3,22,11,0,107,109,3,24,12,0,108,110,
        3,26,13,0,109,108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,
        3,28,14,0,112,111,1,0,0,0,112,113,1,0,0,0,113,21,1,0,0,0,114,115,
        7,0,0,0,115,23,1,0,0,0,116,117,7,1,0,0,117,25,1,0,0,0,118,119,7,
        2,0,0,119,27,1,0,0,0,120,121,7,3,0,0,121,29,1,0,0,0,11,33,40,44,
        54,71,76,83,92,103,109,112
    ]

class AirQualityParser ( Parser ):

    grammarFileName = "AirQualityParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "','", "';'", "':'", "'.'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'+'", "'-'", "'*'", "'/'", "'='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "DATE", "TIME", "FLOAT", "INTEGER", "IDENTIFIER", 
                      "STRING", "PPM", "PPB", "UGM3", "PERCENT", "PM25", 
                      "PM10", "O3", "NO2", "SO2", "CO", "COMMA", "SEMICOLON", 
                      "COLON", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "PLUS", "MINUS", "STAR", "SLASH", 
                      "EQUAL", "NOTEQUAL", "GT", "LT", "GE", "LE", "GOOD", 
                      "MODERATE", "UNHEALTHY", "HAZARDOUS", "WS", "COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_airQualityData = 0
    RULE_record = 1
    RULE_standardRecord = 2
    RULE_jsonRecord = 3
    RULE_jsonField = 4
    RULE_csvRecord = 5
    RULE_field = 6
    RULE_date = 7
    RULE_time = 8
    RULE_measurements = 9
    RULE_measurement = 10
    RULE_pollutant = 11
    RULE_value = 12
    RULE_unit = 13
    RULE_quality = 14

    ruleNames =  [ "airQualityData", "record", "standardRecord", "jsonRecord", 
                   "jsonField", "csvRecord", "field", "date", "time", "measurements", 
                   "measurement", "pollutant", "value", "unit", "quality" ]

    EOF = Token.EOF
    DATE=1
    TIME=2
    FLOAT=3
    INTEGER=4
    IDENTIFIER=5
    STRING=6
    PPM=7
    PPB=8
    UGM3=9
    PERCENT=10
    PM25=11
    PM10=12
    O3=13
    NO2=14
    SO2=15
    CO=16
    COMMA=17
    SEMICOLON=18
    COLON=19
    DOT=20
    LPAREN=21
    RPAREN=22
    LBRACE=23
    RBRACE=24
    LBRACK=25
    RBRACK=26
    PLUS=27
    MINUS=28
    STAR=29
    SLASH=30
    EQUAL=31
    NOTEQUAL=32
    GT=33
    LT=34
    GE=35
    LE=36
    GOOD=37
    MODERATE=38
    UNHEALTHY=39
    HAZARDOUS=40
    WS=41
    COMMENT=42
    BLOCK_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AirQualityDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AirQualityParser.EOF, 0)

        def record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AirQualityParser.RecordContext)
            else:
                return self.getTypedRuleContext(AirQualityParser.RecordContext,i)


        def getRuleIndex(self):
            return AirQualityParser.RULE_airQualityData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAirQualityData" ):
                listener.enterAirQualityData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAirQualityData" ):
                listener.exitAirQualityData(self)




    def airQualityData(self):

        localctx = AirQualityParser.AirQualityDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_airQualityData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.record()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8388734) != 0)):
                    break

            self.state = 35
            self.match(AirQualityParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def standardRecord(self):
            return self.getTypedRuleContext(AirQualityParser.StandardRecordContext,0)


        def jsonRecord(self):
            return self.getTypedRuleContext(AirQualityParser.JsonRecordContext,0)


        def csvRecord(self):
            return self.getTypedRuleContext(AirQualityParser.CsvRecordContext,0)


        def getRuleIndex(self):
            return AirQualityParser.RULE_record

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord" ):
                listener.enterRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord" ):
                listener.exitRecord(self)




    def record(self):

        localctx = AirQualityParser.RecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_record)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.standardRecord()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.jsonRecord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.csvRecord()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StandardRecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def date(self):
            return self.getTypedRuleContext(AirQualityParser.DateContext,0)


        def measurements(self):
            return self.getTypedRuleContext(AirQualityParser.MeasurementsContext,0)


        def time(self):
            return self.getTypedRuleContext(AirQualityParser.TimeContext,0)


        def getRuleIndex(self):
            return AirQualityParser.RULE_standardRecord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandardRecord" ):
                listener.enterStandardRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandardRecord" ):
                listener.exitStandardRecord(self)




    def standardRecord(self):

        localctx = AirQualityParser.StandardRecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_standardRecord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.date()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 43
                self.time()


            self.state = 46
            self.measurements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JsonRecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AirQualityParser.LBRACE, 0)

        def jsonField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AirQualityParser.JsonFieldContext)
            else:
                return self.getTypedRuleContext(AirQualityParser.JsonFieldContext,i)


        def RBRACE(self):
            return self.getToken(AirQualityParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AirQualityParser.COMMA)
            else:
                return self.getToken(AirQualityParser.COMMA, i)

        def getRuleIndex(self):
            return AirQualityParser.RULE_jsonRecord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJsonRecord" ):
                listener.enterJsonRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJsonRecord" ):
                listener.exitJsonRecord(self)




    def jsonRecord(self):

        localctx = AirQualityParser.JsonRecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_jsonRecord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(AirQualityParser.LBRACE)
            self.state = 49
            self.jsonField()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 50
                self.match(AirQualityParser.COMMA)
                self.state = 51
                self.jsonField()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(AirQualityParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JsonFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AirQualityParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(AirQualityParser.COLON, 0)

        def STRING(self):
            return self.getToken(AirQualityParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(AirQualityParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(AirQualityParser.INTEGER, 0)

        def jsonRecord(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AirQualityParser.JsonRecordContext)
            else:
                return self.getTypedRuleContext(AirQualityParser.JsonRecordContext,i)


        def LBRACK(self):
            return self.getToken(AirQualityParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(AirQualityParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AirQualityParser.COMMA)
            else:
                return self.getToken(AirQualityParser.COMMA, i)

        def getRuleIndex(self):
            return AirQualityParser.RULE_jsonField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJsonField" ):
                listener.enterJsonField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJsonField" ):
                listener.exitJsonField(self)




    def jsonField(self):

        localctx = AirQualityParser.JsonFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_jsonField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(AirQualityParser.IDENTIFIER)
            self.state = 60
            self.match(AirQualityParser.COLON)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 61
                self.match(AirQualityParser.STRING)
                pass
            elif token in [3]:
                self.state = 62
                self.match(AirQualityParser.FLOAT)
                pass
            elif token in [4]:
                self.state = 63
                self.match(AirQualityParser.INTEGER)
                pass
            elif token in [23]:
                self.state = 64
                self.jsonRecord()
                pass
            elif token in [25]:
                self.state = 65
                self.match(AirQualityParser.LBRACK)
                self.state = 66
                self.jsonRecord()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 67
                    self.match(AirQualityParser.COMMA)
                    self.state = 68
                    self.jsonRecord()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(AirQualityParser.RBRACK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CsvRecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AirQualityParser.FieldContext)
            else:
                return self.getTypedRuleContext(AirQualityParser.FieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AirQualityParser.COMMA)
            else:
                return self.getToken(AirQualityParser.COMMA, i)

        def getRuleIndex(self):
            return AirQualityParser.RULE_csvRecord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsvRecord" ):
                listener.enterCsvRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsvRecord" ):
                listener.exitCsvRecord(self)




    def csvRecord(self):

        localctx = AirQualityParser.CsvRecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_csvRecord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.field()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 79
                self.match(AirQualityParser.COMMA)
                self.state = 80
                self.field()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AirQualityParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(AirQualityParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(AirQualityParser.INTEGER, 0)

        def IDENTIFIER(self):
            return self.getToken(AirQualityParser.IDENTIFIER, 0)

        def date(self):
            return self.getTypedRuleContext(AirQualityParser.DateContext,0)


        def time(self):
            return self.getTypedRuleContext(AirQualityParser.TimeContext,0)


        def getRuleIndex(self):
            return AirQualityParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = AirQualityParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 86
                self.match(AirQualityParser.STRING)
                pass
            elif token in [3]:
                self.state = 87
                self.match(AirQualityParser.FLOAT)
                pass
            elif token in [4]:
                self.state = 88
                self.match(AirQualityParser.INTEGER)
                pass
            elif token in [5]:
                self.state = 89
                self.match(AirQualityParser.IDENTIFIER)
                pass
            elif token in [1]:
                self.state = 90
                self.date()
                pass
            elif token in [2]:
                self.state = 91
                self.time()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(AirQualityParser.DATE, 0)

        def getRuleIndex(self):
            return AirQualityParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)




    def date(self):

        localctx = AirQualityParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(AirQualityParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME(self):
            return self.getToken(AirQualityParser.TIME, 0)

        def getRuleIndex(self):
            return AirQualityParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = AirQualityParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(AirQualityParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasurementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def measurement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AirQualityParser.MeasurementContext)
            else:
                return self.getTypedRuleContext(AirQualityParser.MeasurementContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AirQualityParser.SEMICOLON)
            else:
                return self.getToken(AirQualityParser.SEMICOLON, i)

        def getRuleIndex(self):
            return AirQualityParser.RULE_measurements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasurements" ):
                listener.enterMeasurements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasurements" ):
                listener.exitMeasurements(self)




    def measurements(self):

        localctx = AirQualityParser.MeasurementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_measurements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.measurement()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 99
                self.match(AirQualityParser.SEMICOLON)
                self.state = 100
                self.measurement()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasurementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pollutant(self):
            return self.getTypedRuleContext(AirQualityParser.PollutantContext,0)


        def value(self):
            return self.getTypedRuleContext(AirQualityParser.ValueContext,0)


        def unit(self):
            return self.getTypedRuleContext(AirQualityParser.UnitContext,0)


        def quality(self):
            return self.getTypedRuleContext(AirQualityParser.QualityContext,0)


        def getRuleIndex(self):
            return AirQualityParser.RULE_measurement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasurement" ):
                listener.enterMeasurement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasurement" ):
                listener.exitMeasurement(self)




    def measurement(self):

        localctx = AirQualityParser.MeasurementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_measurement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.pollutant()
            self.state = 107
            self.value()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0):
                self.state = 108
                self.unit()


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2061584302080) != 0):
                self.state = 111
                self.quality()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PollutantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PM25(self):
            return self.getToken(AirQualityParser.PM25, 0)

        def PM10(self):
            return self.getToken(AirQualityParser.PM10, 0)

        def O3(self):
            return self.getToken(AirQualityParser.O3, 0)

        def NO2(self):
            return self.getToken(AirQualityParser.NO2, 0)

        def SO2(self):
            return self.getToken(AirQualityParser.SO2, 0)

        def CO(self):
            return self.getToken(AirQualityParser.CO, 0)

        def IDENTIFIER(self):
            return self.getToken(AirQualityParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return AirQualityParser.RULE_pollutant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPollutant" ):
                listener.enterPollutant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPollutant" ):
                listener.exitPollutant(self)




    def pollutant(self):

        localctx = AirQualityParser.PollutantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pollutant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129056) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(AirQualityParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(AirQualityParser.INTEGER, 0)

        def getRuleIndex(self):
            return AirQualityParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = AirQualityParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PPM(self):
            return self.getToken(AirQualityParser.PPM, 0)

        def PPB(self):
            return self.getToken(AirQualityParser.PPB, 0)

        def UGM3(self):
            return self.getToken(AirQualityParser.UGM3, 0)

        def PERCENT(self):
            return self.getToken(AirQualityParser.PERCENT, 0)

        def getRuleIndex(self):
            return AirQualityParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = AirQualityParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOOD(self):
            return self.getToken(AirQualityParser.GOOD, 0)

        def MODERATE(self):
            return self.getToken(AirQualityParser.MODERATE, 0)

        def UNHEALTHY(self):
            return self.getToken(AirQualityParser.UNHEALTHY, 0)

        def HAZARDOUS(self):
            return self.getToken(AirQualityParser.HAZARDOUS, 0)

        def getRuleIndex(self):
            return AirQualityParser.RULE_quality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuality" ):
                listener.enterQuality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuality" ):
                listener.exitQuality(self)




    def quality(self):

        localctx = AirQualityParser.QualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_quality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2061584302080) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






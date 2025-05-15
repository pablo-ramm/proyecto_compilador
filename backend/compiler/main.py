import os
import sys
import re
import json
import csv
import pandas as pd
from datetime import datetime
from antlr4 import *

from antlr4.tree.Trees import Trees


def parse_fecha(fecha_str):
    input_stream = InputStream(fecha_str)
    lexer = FechaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FechaParser(stream)
    tree = parser.fecha()

    stream.fill()
    # Ignorar separadores como espacios, comas, /, -
    tokens = [t.text for t in stream.tokens if t.type not in {FechaLexer.WS, FechaLexer.COMA} and t.text not in {'/', '-', '<EOF>'}]
    print("Tokens:", tokens)

    try:
        if '/' in fecha_str:
            mes, dia, anio = tokens
        elif '-' in fecha_str:
            if len(tokens[0]) == 4:
                anio, mes, dia = tokens
            else:
                dia, mes, anio = tokens
        else:
            if tokens[0].isdigit():
                dia = tokens[0]
                mes = MES_TEXTO_MAP.get(tokens[1].lower(), tokens[1])  # puede ser número o texto
                anio = tokens[2]
            else:
                mes = MES_TEXTO_MAP.get(tokens[0].lower(), tokens[0])
                dia = tokens[1]
                anio = tokens[2]

        # Validar fecha usando datetime
        fecha_valida = datetime(int(anio), int(mes), int(dia))
        return fecha_valida.strftime("%Y-%m-%d")

    except (ValueError, IndexError, KeyError) as e:
        print("Error:", e)
        return "Formato no reconocido"


MES_TEXTO_MAP = {
    'ene': '01', 'enero': '01', 'feb': '02', 'febrero': '02',
    'mar': '03', 'marzo': '03', 'abr': '04', 'abril': '04',
    'may': '05', 'mayo': '05', 'jun': '06', 'junio': '06',
    'jul': '07', 'julio': '07', 'ago': '08', 'agosto': '08',
    'sep': '09', 'septiembre': '09', 'oct': '10', 'octubre': '10',
    'nov': '11', 'noviembre': '11', 'dic': '12', 'diciembre': '12',
}

from datetime import datetime

def parse_fecha(fecha_str):
    input_stream = InputStream(fecha_str)
    lexer = FechaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FechaParser(stream)
    tree = parser.fecha()

    stream.fill()
    # Ignorar separadores como espacios, comas, /, -
    tokens = [t.text for t in stream.tokens if t.type not in {FechaLexer.WS, FechaLexer.COMA} and t.text not in {'/', '-', '<EOF>'}]
    print("Tokens:", tokens)

    try:
        if '/' in fecha_str:
            mes, dia, anio = tokens
        elif '-' in fecha_str:
            if len(tokens[0]) == 4:
                anio, mes, dia = tokens
            else:
                dia, mes, anio = tokens
        else:
            if tokens[0].isdigit():
                dia = tokens[0]
                mes = MES_TEXTO_MAP.get(tokens[1].lower(), tokens[1])  # puede ser número o texto
                anio = tokens[2]
            else:
                mes = MES_TEXTO_MAP.get(tokens[0].lower(), tokens[0])
                dia = tokens[1]
                anio = tokens[2]

        # Validar fecha usando datetime
        fecha_valida = datetime(int(anio), int(mes), int(dia))
        return fecha_valida.strftime("%Y-%m-%d")

    except (ValueError, IndexError, KeyError) as e:
        print("Error:", e)
        return "Formato no reconocido"

def convertir_ml_a_l_o_viceversa(texto):
    input_stream = InputStream(texto)
    lexer = MLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MLParser(stream)
    tree = parser.expr()

    # Accede directamente a los hijos del árbol
    amount_ctx = tree.getChild(0)  # cantidad
    unit_ctx = tree.getChild(1)    # unidad

    valor = float(amount_ctx.getText())
    unidad = unit_ctx.getText()

    if unidad == "ml":
        return f"{valor / 1000}L"
    elif unidad == "L":
        return f"{valor * 1000}ml"
    else:
        raise ValueError("Unidad no reconocida.")

exchange_rates = {
    'USD': 1.0,
    'EUR': 1.1,
    'GBP': 1.3,
    'JPY': 0.007,
    '$': 1.0,
    '€': 1.1,
    '£': 1.3,
    '¥': 0.007
}

def convert_to_usd(amount, currency):
    rate = exchange_rates.get(currency)
    return amount * rate if rate else None

def parse_currency(text):
    input_stream = InputStream(text)
    lexer = CurrencyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CurrencyParser(stream)
    tree = parser.currencyExpr()

    tokens = [t.text for t in stream.tokens if t.channel == Token.DEFAULT_CHANNEL]

    # Identificamos el número y la moneda
    number = float([t for t in tokens if t.replace('.', '', 1).isdigit()][0])
    currency = [t for t in tokens if t in exchange_rates][0]

    usd = convert_to_usd(number, currency)
    return f"{text} → {usd:.2f} USD"

# Example usage
def main():
    

if __name__ == "__main__":
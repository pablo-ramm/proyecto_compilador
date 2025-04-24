import os
import sys
import re
import json
import csv
import pandas as pd
from datetime import datetime
from antlr4 import *
from AirQualityLexer import AirQualityLexer
from AirQualityParser import AirQualityParser
from antlr4.tree.Trees import Trees

class AirQualityNormalizer:
    """
    Class to normalize air quality data using ANTLR for syntactic analysis
    """
    
    # Standard pollutant names
    STANDARD_POLLUTANTS = {
        'PM2.5': ['PM2.5', 'pm2.5', 'PM2_5', 'pm2_5', 'fine particulate matter'],
        'PM10': ['PM10', 'pm10', 'particulate matter'],
        'O3': ['O3', 'o3', 'ozone', 'OZONE'],
        'NO2': ['NO2', 'no2', 'nitrogen dioxide', 'NITROGEN DIOXIDE'],
        'SO2': ['SO2', 'so2', 'sulfur dioxide', 'SULFUR DIOXIDE'],
        'CO': ['CO', 'co', 'carbon monoxide', 'CARBON MONOXIDE']
    }
    
    # Standard units and conversion factors (to convert to standard units)
    STANDARD_UNITS = {
        'PM2.5': 'µg/m³',
        'PM10': 'µg/m³',
        'O3': 'ppb',
        'NO2': 'ppb',
        'SO2': 'ppb',
        'CO': 'ppm'
    }
    
    # Conversion factors
    CONVERSION_FACTORS = {
        'O3': {'ppm': 1000, 'ppb': 1},  # 1 ppm = 1000 ppb
        'NO2': {'ppm': 1000, 'ppb': 1},
        'SO2': {'ppm': 1000, 'ppb': 1},
        'CO': {'ppb': 0.001, 'ppm': 1}  # 1 ppb = 0.001 ppm
    }
    
    def __init__(self, db_path=None):
        """
        Initialize the normalizer
        
        Args:
            db_path: Path to the database file or directory
        """
        self.db_path = db_path
        self.normalized_data = []
    
    def normalize_pollutant_name(self, name):
        """
        Normalize pollutant name to standard format
        
        Args:
            name: The pollutant name to normalize
            
        Returns:
            Standardized pollutant name
        """
        for standard, variants in self.STANDARD_POLLUTANTS.items():
            if name in variants:
                return standard
        
        return name  # Return as is if not found
    
    def convert_to_standard_unit(self, pollutant, value, unit):
        """
        Convert value to standard unit for the pollutant
        
        Args:
            pollutant: The pollutant name
            value: The numeric value
            unit: The current unit
            
        Returns:
            Value converted to standard unit
        """
        standard_pollutant = self.normalize_pollutant_name(pollutant)
        
        # If the pollutant is not one we know, return as is
        if standard_pollutant not in self.STANDARD_UNITS:
            return value
            
        # If unit is already standard, return as is
        standard_unit = self.STANDARD_UNITS[standard_pollutant]
        if unit == standard_unit:
            return value
            
        # If we need to convert
        if standard_pollutant in self.CONVERSION_FACTORS and unit in self.CONVERSION_FACTORS[standard_pollutant]:
            factor = self.CONVERSION_FACTORS[standard_pollutant][unit]
            return value * factor
            
        # No conversion possible, return as is
        return value
    
    def normalize_quality(self, quality_str):
        """
        Normalize air quality category
        
        Args:
            quality_str: Quality string to normalize
            
        Returns:
            Standardized quality category
        """
        quality_map = {
            'good': 'Good',
            'moderate': 'Moderate',
            'unhealthy': 'Unhealthy',
            'hazardous': 'Hazardous'
        }
        
        if quality_str.lower() in quality_map:
            return quality_map[quality_str.lower()]
        
        return quality_str
    
    def parse_and_normalize(self, input_data):
        """
        Parse and normalize air quality data using ANTLR
        
        Args:
            input_data: Raw input data string
            
        Returns:
            Normalized data dictionary
        """
        # Create ANTLR lexer and parser
        input_stream = InputStream(input_data)
        lexer = AirQualityLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = AirQualityParser(token_stream)
        
        # Parse data
        tree = parser.airQualityData()
        
        # Custom listener to extract and normalize data
        class AirQualityListener(ParseTreeListener):
            def __init__(self, normalizer):
                self.normalizer = normalizer
                self.current_record = {}
                self.normalized_records = []
                
            def enterStandardRecord(self, ctx):
                self.current_record = {'type': 'standard'}
                
            def exitStandardRecord(self, ctx):
                self.normalized_records.append(self.current_record.copy())
                
            def enterJsonRecord(self, ctx):
                self.current_record = {'type': 'json'}
                
            def exitJsonRecord(self, ctx):
                self.normalized_records.append(self.current_record.copy())
                
            def enterCsvRecord(self, ctx):
                self.current_record = {'type': 'csv'}
                
            def exitCsvRecord(self, ctx):
                self.normalized_records.append(self.current_record.copy())
                
            def enterDate(self, ctx):
                if ctx.DATE():
                    self.current_record['date'] = ctx.DATE().getText()
                    
            def enterTime(self, ctx):
                if ctx.TIME():
                    self.current_record['time'] = ctx.TIME().getText()
                    
            def enterMeasurement(self, ctx):
                if ctx.pollutant() and ctx.value():
                    pollutant_ctx = ctx.pollutant()
                    pollutant = None
                    
                    # Extract pollutant
                    for pollutant_type in ['PM25', 'PM10', 'O3', 'NO2', 'SO2', 'CO']:
                        if getattr(pollutant_ctx, pollutant_type, None)() is not None:
                            pollutant = getattr(pollutant_ctx, pollutant_type)().getText()
                            break
                    
                    if pollutant is None and pollutant_ctx.IDENTIFIER():
                        pollutant = pollutant_ctx.IDENTIFIER().getText()
                    
                    # Extract value
                    value_ctx = ctx.value()
                    if value_ctx.FLOAT():
                        value = float(value_ctx.FLOAT().getText())
                    elif value_ctx.INTEGER():
                        value = int(value_ctx.INTEGER().getText())
                    else:
                        value = None
                    
                    # Extract unit if present
                    unit = None
                    if ctx.unit():
                        unit_ctx = ctx.unit()
                        for unit_type in ['PPM', 'PPB', 'UGM3', 'PERCENT']:
                            if getattr(unit_ctx, unit_type, None)() is not None:
                                unit = getattr(unit_ctx, unit_type)().getText()
                                break
                    
                    # Extract quality if present
                    quality = None
                    if ctx.quality():
                        quality_ctx = ctx.quality()
                        for quality_type in ['GOOD', 'MODERATE', 'UNHEALTHY', 'HAZARDOUS']:
                            if getattr(quality_ctx, quality_type, None)() is not None:
                                quality = getattr(quality_ctx, quality_type)().getText()
                                break
                    
                    # Normalize the data
                    if pollutant and value is not None:
                        normalized_pollutant = self.normalizer.normalize_pollutant_name(pollutant)
                        
                        if unit:
                            normalized_value = self.normalizer.convert_to_standard_unit(
                                normalized_pollutant, value, unit
                            )
                        else:
                            normalized_value = value
                        
                        if quality:
                            normalized_quality = self.normalizer.normalize_quality(quality)
                        else:
                            normalized_quality = None
                        
                        # Add to current record
                        if 'measurements' not in self.current_record:
                            self.current_record['measurements'] = []
                            
                        self.current_record['measurements'].append({
                            'pollutant': normalized_pollutant,
                            'value': normalized_value,
                            'unit': self.normalizer.STANDARD_UNITS.get(normalized_pollutant, unit),
                            'quality': normalized_quality
                        })
        
        # Walk the parse tree with our listener
        listener = AirQualityListener(self)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        return listener.normalized_records
    
    def process_file(self, file_path):
        """
        Process a single file and normalize its data
        
        Args:
            file_path: Path to the file to process
            
        Returns:
            List of normalized records
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Detect file type based on extension
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.json':
            try:
                # Try to parse as JSON
                data = json.loads(content)
                # Convert JSON to string format our parser can handle
                content = json.dumps(data)
            except json.JSONDecodeError:
                pass  # Not valid JSON, continue with normal parsing
        
        elif file_ext == '.csv':
            try:
                # Try to parse as CSV
                reader = csv.reader(content.splitlines())
                rows = list(reader)
                # Convert CSV to string format our parser can handle
                content = '\n'.join([','.join(row) for row in rows])
            except Exception:
                pass  # Not valid CSV, continue with normal parsing
        
        # Parse and normalize using ANTLR
        try:
            normalized_records = self.parse_and_normalize(content)
            self.normalized_data.extend(normalized_records)
            return normalized_records
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            return []
    
    def process_database(self):
        """
        Process all files in the database directory
        
        Returns:
            DataFrame with all normalized data
        """
        if not self.db_path:
            raise ValueError("Database path not specified")
            
        if os.path.isdir(self.db_path):
            # Process all files in directory
            for root, dirs, files in os.walk(self.db_path):
                for file in files:
                    if file.endswith(('.txt', '.json', '.csv')):
                        file_path = os.path.join(root, file)
                        self.process_file(file_path)
        elif os.path.isfile(self.db_path):
            # Process single file
            self.process_file(self.db_path)
        else:
            raise FileNotFoundError(f"Database path {self.db_path} not found")
            
        # Convert to DataFrame
        return self.to_dataframe()
    
    def to_dataframe(self):
        """
        Convert normalized data to a pandas DataFrame
        
        Returns:
            DataFrame with normalized data
        """
        # Flatten the nested structure
        flattened_data = []
        
        for record in self.normalized_data:
            base_record = {
                'date': record.get('date'),
                'time': record.get('time')
            }
            
            if 'measurements' in record:
                for measurement in record['measurements']:
                    data_point = base_record.copy()
                    data_point.update({
                        'pollutant': measurement['pollutant'],
                        'value': measurement['value'],
                        'unit': measurement['unit'],
                        'quality': measurement['quality']
                    })
                    flattened_data.append(data_point)
            else:
                flattened_data.append(base_record)
        
        return pd.DataFrame(flattened_data)
    
    def save_to_csv(self, output_path):
        """
        Save normalized data to CSV
        
        Args:
            output_path: Path to save the CSV file
        """
        df = self.to_dataframe()
        df.to_csv(output_path, index=False)
    
    def save_to_json(self, output_path):
        """
        Save normalized data to JSON
        
        Args:
            output_path: Path to save the JSON file
        """
        df = self.to_dataframe()
        df.to_json(output_path, orient='records', indent=2)

# Example usage
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Normalize air quality data using ANTLR')
    parser.add_argument('--input', '-i', required=True, help='Input file or directory path')
    parser.add_argument('--output', '-o', required=True, help='Output file path')
    parser.add_argument('--format', '-f', choices=['csv', 'json'], default='csv', help='Output format')
    
    args = parser.parse_args()
    
    normalizer = AirQualityNormalizer(args.input)
    normalizer.process_database()
    
    if args.format == 'csv':
        normalizer.save_to_csv(args.output)
    else:
        normalizer.save_to_json(args.output)
    
    print(f"Normalized data saved to {args.output}")

if __name__ == "__main__":
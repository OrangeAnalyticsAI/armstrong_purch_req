import pandas as pd
from typing import Dict, List

class ColumnMapper:
    """Maps various possible column names to standardized names"""
    
    COLUMN_MAPPINGS = {
        'item_no': ['Item no', 'Item nr', 'Item no.', 'Item number', 'Item'],
        'quantity': ['Qty', 'Quantity'],
        'description': ['Description'],
        'length_mm': ['Length', 'Length(mm)', 'Length (mm)'],
        'drilling_detail': ['Drilling detail', 'Drilling'],
        'assembly_time': ['Assembly time', 'Assy time'],
        'weight_kg': ['Weight', 'Weight(Kg)', 'Weight (kg)']
    }
    
    @classmethod
    def guess_column_mapping(cls, df_columns: List[str]) -> Dict[str, str]:
        """
        Attempts to automatically map input columns to standard column names
        Returns a dictionary of {input_column: standard_column}
        """
        mapping = {}
        for std_col, possible_names in cls.COLUMN_MAPPINGS.items():
            for col in df_columns:
                if col.strip().lower() in [name.strip().lower() for name in possible_names]:
                    mapping[col] = std_col
        return mapping

class FileProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def read_file(self) -> pd.DataFrame:
        """Read Excel or CSV file based on extension"""
        if self.file_path.endswith('.csv'):
            return pd.read_csv(self.file_path)
        elif self.file_path.endswith(('.xlsx', '.xls')):
            return pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Excel.")
            
    def process_file(self) -> tuple[pd.DataFrame, Dict[str, str]]:
        """
        Process the input file and return the DataFrame and suggested column mappings
        """
        df = self.read_file()
        suggested_mappings = ColumnMapper.guess_column_mapping(df.columns)
        
        return df, suggested_mappings 
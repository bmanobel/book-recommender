import pandas as pd

class BookDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        # Load the original CSV file
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()

        required_cols = {'Name', 'Genres'}
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        synopsis_column = None
        for candidate in ('synopsis', 'sypnopsis'):
            if candidate in df.columns:
                synopsis_column = candidate
                break

        if synopsis_column is None:
            raise ValueError("Missing required columns: {'synopsis'}")
        
        df['combined_info'] = (
            "Title: " + df["Name"].astype(str) + " Overview: " + df[synopsis_column].astype(str) + " Genres: " + df["Genres"].astype(str)
        )
        # Process the data (for example, we can drop duplicates and handle missing values)
        df[["combined_info"]].to_csv(self.processed_csv, index=False, encoding ='utf-8')



        return self.processed_csv
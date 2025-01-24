from file_processor import FileProcessor
from models import Base, PurchaseRequisition
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    # Initialize database
    engine = create_engine('sqlite:///purchase_system.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    
    # Get file path from user
    file_path = input("Enter the path to your Excel/CSV file: ")
    
    try:
        # Process file
        processor = FileProcessor(file_path)
        df, suggested_mappings = processor.process_file()
        
        # Show columns and suggested mappings
        print("\nFound columns:", df.columns.tolist())
        print("\nSuggested mappings:")
        for original, suggested in suggested_mappings.items():
            print(f"{original} -> {suggested}")
        
        # Allow user to modify mappings
        print("\nWould you like to modify any mappings? (y/n)")
        if input().lower() == 'y':
            # Add code for manual mapping here
            pass
            
        # Preview data
        print("\nFirst few rows of data:")
        print(df.head())
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main() 
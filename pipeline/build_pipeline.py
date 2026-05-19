from src.data_loader import BookDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the Book Recommendation Pipeline...")
        
        # Step 1: Load and process the data
        loader = BookDataLoader(
            original_csv="data/recomendaciones_libros_reales_1000.csv",
            processed_csv="data/book_updated.csv"
        )
        processed_csv = loader.load_and_process()
        logger.info(f"Data loaded and processed successfully. Processed file: {processed_csv}")
        
        # Step 2: Build and save the vector store
        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector store built and saved successfully.")
        
    except Exception as e:
        logger.error(f"Error in main pipeline execution: {e}")
        raise CustomException(f"Error during pipeline execution: {e}")


if __name__ == "__main__":
    main()
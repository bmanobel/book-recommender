from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path:str,  persist_dir:str="chroma_db"):
        self.processed_csv = csv_path
        self.persist_dir = persist_dir
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def build_and_save_vectorstore(self):
        # Load the processed CSV file
        loader = CSVLoader(
            file_path=self.processed_csv,       
            encoding='utf-8',
            metadata_columns=[]
            )
        data = loader.load()

        # Split the text into smaller chunks
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        # Create embeddings using HuggingFaceEmbeddings
        embeddings = self.embeddings

        # Create a Chroma vector store and persist it to disk
        db = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,   
            persist_directory=self.persist_dir
        )
        
    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)
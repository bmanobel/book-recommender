from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from pipeline.pipeline import BookRecommendationPipeline
from dotenv import load_dotenv




load_dotenv()


def main():    
    st.title("Book Recommender System")
    st.write("Welcome to the Book Recommender System! Enter your preferences to get personalized book recommendations.")

    @st.cache_resource
    def init_pipeline():
        return BookRecommendationPipeline()

    pipeline = init_pipeline()


    query = st.text_input("Enter your book preferences (e.g., 'I like literary fiction with strong character development'):")
    if query:
        with st.spinner("Generating recommendations..."):
            response = pipeline.recommend(query)
            st.markdown("### Recommended Books:")
            st.write(response)
            
if __name__ == "__main__":
    main()
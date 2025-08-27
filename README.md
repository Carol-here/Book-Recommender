Semantic Book Recommender
A semantic book recommendation system built using Python, LangChain, Chroma, and Gradio. Users can input a short description of a book and receive recommendations based on emotional tone and category.

Features:
Semantic Search: Uses embeddings to find books that match the meaning of user input.
Emotion-Based Filtering: Recommendations can be filtered by emotional tones such as Happy, Sad, Suspenseful, Angry, and Surprising.
Category Filtering: Filter recommendations by book category.
Interactive UI: Simple Gradio interface with thumbnails and captions.

Tech Stack:
Python 3.10+
LangChain & Chroma for embeddings and vector database.
Sentence Transformers for lightweight embeddings (all-MiniLM-L6-v2) to run locally without requiring large models.
Gradio for an interactive front-end.
Pandas & NumPy for data handling.

Customizations Made:
This project started as a tutorial, but I made several adaptations for efficiency and usability:
Used smaller models (Sentence Transformers) instead of large Hugging Face models to run efficiently on CPU.

Adjusted embedding and Chroma code for local execution.
Updated the UI layout and interactions slightly for ease of use.
These changes show my ability to adapt tutorials into working projects on my own setup.

Data:
books_with_emotions.csv – Book metadata including emotional tone tags.
tagged_description_clean.txt – Preprocessed book descriptions for embeddings in utf-8 format.
tagged_description.txt- Preprocessed book description for embeddings
Both files are included in the repo (or can be regenerated from the original datasets if large).

How to Run

Clone the repository:

git clone https://github.com/Carol-here/Book-Recommender.git
cd Book-Recommender

Create a virtual environment and install dependencies:

python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt


Run the Gradio app:
python UI.py
Open the link shown in your terminal to interact with the recommender.

Future Improvements:
Integrate larger language models for more accurate embeddings.
Add more advanced emotion recognition from book descriptions.
Make UI more interactive with hover effects and highlighted thumbnails.

License:
This project is for learning and portfolio purposes.

from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

app = Flask(__name__, static_folder='static')

# Create static/images directory if it doesn't exist
os.makedirs(os.path.join(app.static_folder, 'images'), exist_ok=True)

# Read book data from CSV file
books_df = pd.read_csv('books.csv')

# Create TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books_df['description'])

@app.route('/')
def home():
    # Add static URL for images
    books_data = books_df.to_dict('records')
    for book in books_data:
        if not book['image_url'].startswith(('http://', 'https://')):
            book['image_url'] = url_for('static', filename=f"images/{book['image_url']}")
    return render_template('index.html', books=books_data)

@app.route('/recommend', methods=['POST'])
def recommend():
    book_title = request.form.get('book_title')
    
    # Find the book index
    book_idx = books_df[books_df['title'] == book_title].index[0]
    
    # Calculate similarity scores
    cosine_sim = cosine_similarity(tfidf_matrix[book_idx:book_idx+1], tfidf_matrix)
    
    # Get similar book indices
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 similar books
    
    # Get book indices
    book_indices = [i[0] for i in sim_scores]
    
    # Return recommended books with proper image URLs
    recommendations = books_df.iloc[book_indices].to_dict('records')
    for book in recommendations:
        if not book['image_url'].startswith(('http://', 'https://')):
            book['image_url'] = url_for('static', filename=f"images/{book['image_url']}")
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

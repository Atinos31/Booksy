from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://openlibrary.org/search.json?q=the+lord+of+the+rings')
    books = response.json()['docs'][:10]  # Get the first 10 books
    # Add logic to construct cover image URLs
    for book in books:
        if 'cover_i' in book:
            book['cover_url'] = f"https://covers.openlibrary.org/b/id/{book['cover_i']}-M.jpg"
        else:
            book['cover_url'] = "https://via.placeholder.com/100x140"

    return render_template('index.html', books=books)

@app.route('/book/<book_id>')
def book_details(book_id):
    response = requests.get(f'http://openlibrary.org/books/{book_id}.json')
    book = response.json()
    # Handling for cover image in details
    if 'covers' in book:
        book['cover_url'] = f"https://covers.openlibrary.org/b/id/{book['covers'][0]}-L.jpg"
    else:
        book['cover_url'] = "https://via.placeholder.com/100x140"

    return render_template('details.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)

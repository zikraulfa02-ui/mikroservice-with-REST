from flask import Flask, jsonify

app = Flask(__name__)

# Database khusus Book Service
books = [
    {
        "id": 1,
        "title": "Belajar Flask",
        "stock": 5
    }
]


# Menampilkan semua buku
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Menampilkan buku berdasarkan ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for b in books:
        if b['id'] == book_id:
            return jsonify(b)

    return jsonify({
        "error": "Not found"
    }), 404


# Menjalankan Book Service
if __name__ == '__main__':
    print("======================================")
    print("          BOOK SERVICE")
    print("======================================")
    print("Server berjalan di:")
    print("http://localhost:5001")
    print("======================================")

    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )
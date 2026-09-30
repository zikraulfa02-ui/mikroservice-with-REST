from flask import Flask, jsonify, request

app = Flask(__name__)

# ==========================================
# DATABASE BOHONGAN (IN-MEMORY)
# ==========================================

books = [
    {
        "id": 1,
        "title": "Belajar Flask",
        "stock": 5
    }
]

orders = []


# ==========================================
# FITUR BUKU
# ==========================================

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# ==========================================
# FITUR PESANAN
# ==========================================

@app.route('/orders', methods=['POST'])
def create_order():

    # Mengambil data JSON dari request
    data = request.get_json()

    # Mengambil book_id
    book_id = data.get('book_id')

    # Mengecek buku dan stok
    for b in books:

        if b['id'] == book_id and b['stock'] > 0:

            # Mengurangi stok buku
            b['stock'] -= 1

            # Membuat pesanan baru
            order = {
                "id": len(orders) + 1,
                "book_id": book_id,
                "status": "berhasil"
            }

            # Menyimpan pesanan
            orders.append(order)

            # Mengembalikan response
            return jsonify(order), 201

    # Jika buku tidak ditemukan atau stok habis
    return jsonify({
        "error": "Buku tidak ditemukan atau stok habis"
    }), 400


# ==========================================
# MENJALANKAN APLIKASI
# ==========================================

if __name__ == '__main__':

    print("======================================")
    print("   APLIKASI MONOLITH FLASK")
    print("======================================")
    print("Server berjalan di:")
    print("http://localhost:5000")
    print("======================================")

    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
    
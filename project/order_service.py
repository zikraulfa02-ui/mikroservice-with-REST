from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Penyimpanan pesanan
orders = []

# Alamat Book Service
BOOK_SERVICE_URL = "http://localhost:5001"


# Membuat pesanan
@app.route('/orders', methods=['POST'])
def create_order():

    # Mengambil data JSON
    data = request.get_json()

    # Mengambil ID buku
    book_id = data.get('book_id')

    # Menghubungi Book Service
    try:
        response = requests.get(
            f"{BOOK_SERVICE_URL}/books/{book_id}"
        )

        # Jika buku ditemukan
        if response.status_code == 200:

            book_data = response.json()

            # Mengecek stok
            if book_data['stock'] > 0:

                # Membuat pesanan
                order = {
                    "id": len(orders) + 1,
                    "book_id": book_id,
                    "status": "berhasil"
                }

                # Menyimpan pesanan
                orders.append(order)

                return jsonify(order), 201

        # Jika buku tidak tersedia
        return jsonify({
            "error": "Buku tidak tersedia"
        }), 400

    # Jika Book Service mati
    except requests.exceptions.ConnectionError:

        return jsonify({
            "error": "Book Service sedang down!"
        }), 500


# Menjalankan Order Service
if __name__ == '__main__':
    print("======================================")
    print("          ORDER SERVICE")
    print("======================================")
    print("Server berjalan di:")
    print("http://localhost:5002")
    print("======================================")

    app.run(
        host='127.0.0.1',
        port=5002,
        debug=True
    )
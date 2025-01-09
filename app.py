# Importowanie Flask i innych potrzebnych bibliotek
from flask import Flask, render_template

# Tworzenie instancji aplikacji Flask
app = Flask(__name__)

# Przykładowe dane: lista książek
books = [
    {"id": 1, "title": "W pustyni i w puszczy", "author": "Henryk Sienkiewicz", "description": "Przygody Stasia i Nel w Afryce."},
    {"id": 2, "title": "Pan Tadeusz", "author": "Adam Mickiewicz", "description": "Epopeja narodowa opowiadająca o życiu szlachty polskiej."},
    {"id": 3, "title": "Lalka", "author": "Bolesław Prus", "description": "Historia Stanisława Wokulskiego i jego niespełnionej miłości."}
]

# Strona główna: lista książek
@app.route('/')
def home():
    return render_template('home.html', books=books)

# Strona szczegółów książki
@app.route('/book/<int:book_id>')
def book_details(book_id):
    # Wyszukanie książki po ID
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return render_template('book_details.html', book=book)
    else:
        return "Książka nie znaleziona", 404

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

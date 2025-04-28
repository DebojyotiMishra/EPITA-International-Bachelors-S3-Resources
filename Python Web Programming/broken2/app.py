# Fixes:
# 1. Importing reder_template from flask
# 2. from "models" -> from "model"
# 3. "Books" -> "Book"
# 4. "Borrows" -> "Borrow"
# 5. "@app.route('/books/delete/<boolean:id>')" -> @app.route('/books/delete/<int:id>')
# 6. Added POST method to edit_book route
# 7. Corrected the methods in the borrow route -> the quotation marks were wrong
# 8. Added app.run to the end of the file because we can't run the app without it
# 9. its was books.html for /books route
# 10. Book.query.all() instead of Book.all()
# 11. in the borrow/return route: db.session.delete(borrow), db.session.commit()

from flask import Flask, request, redirect, url_for, flash, render_template
from model import db, Book, Borrow
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "b2c4e2d9f7a3d6f1e2c4b8a9d7f3c4e6"

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    all_books = Book.query.all()
    return render_template("books.html", books=all_books)

@app.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        print(request.form)
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]

        book = Book(title=title, author=author, year=year)
        db.session.add(book)
        db.session.commit()

        flash("Book added successfully!")
        return redirect(url_for("books"))

    return render_template("add_book.html")


@app.route("/books/<int:id>/edit", methods=["GET", "POST"])
def edit_book(id):
    book = Book.query.get(id)
    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.year = request.form["year"]

        db.session.commit()
        flash("Livre modifié avec succès!")
        return redirect(url_for("books"))

    return render_template("edit_book.html", book=book)


@app.route("/books/<int:id>/delete")
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash("Book Deleted!")
    return redirect(url_for("books"))


@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    books = Book.query.all()
    borrows = Borrow.query.all()
    
    if request.method == 'POST':
        book_id = request.form['book_id']
        borrower_name = request.form['borrower_name']

        borrow = Borrow(book_id=book_id, borrower_name=borrower_name)
        db.session.add(borrow)
        db.session.commit()

        flash('Borrow saved successfully!')
        return redirect(url_for('borrow'))

    return render_template('borrow.html', books=books, borrows=borrows)

@app.route("/borrow/return/<int:id>")
def return_book(id):
    borrow = Borrow.query.get(id)
    db.session.delete(borrow)
    db.session.commit()
    flash("book return success!")
    return redirect(url_for("borrow"))


if __name__ == "__main__":
    print("launch ok")
    app.run(port=8000, debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/ASUS/Desktop/Library Project/new_book_collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Optional, to suppress a warning

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    note = db.Column(db.String(100), nullable=True)

@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
            note=request.form["note"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get_or_404(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get_or_404(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete/<int:id>")
def delete(id):
    book_to_delete = Book.query.get_or_404(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database and tables
    app.run(debug=True)

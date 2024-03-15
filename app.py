from flask import Flask, render_template, session, redirect, url_for, g
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignUpForm, LoginForm, ReviewsForm, FinaliseCart
from functools import wraps

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)

def login_required(view):
    @wraps(view)
    def wrapper(**kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return view(**kwargs)
    return wrapper

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/collections")
def collections():
    return render_template("collections.html")

    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        possible_clashing_user = db.execute(
            """SELECT * FROM users
             WHERE user_id = ?""",
            (user_id, )).fetchone()
        if possible_clashing_user is not None:
            form.user_id.errors.append("User id is already taken")
        else:
            db.execute(
                """INSERT INTO users (user_id, password)
                          VALUES (?,?);""",
                (user_id, generate_password_hash(password)))
            db.commit()
            return redirect(url_for("login"))
    return render_template("signup.html", form=form)

@app.route("/shop")
def shop():
    db = get_db()
    products = db.execute("""SELECT *  FROM products;""")
    return render_template("shop.html", products = products)
    
@app.route("/add_to_cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = {}
    if product_id not in session["cart"]:
        session["cart"][product_id] = 0
    session["cart"][product_id] = session["cart"][product_id] + 1
    return redirect (url_for("cart"))

@app.route("/removeitem/<int:product_id>")
def removeitem(product_id):
    if product_id in session["cart"]:
        if session["cart"][product_id] == 1:
            session["cart"].pop(product_id)
        else:
            session["cart"][product_id] -= 1

        return redirect(url_for('cart'))

@app.route("/cart")
@login_required
def cart():
    if "cart" not in session:
        session["cart"] = {}
    names = {}
    prices = {}
    imgs = {}
    total = 0
    db = get_db()
    for product_id in session["cart"]:
        product = db.execute("""SELECT * FROM products
                                WHERE product_id = ?;""",(product_id,)).fetchone()
        name = product["name"]
        img = product["img"]
        price = product["price"]
        imgs[product_id] = img
        names[product_id] = name
        prices[product_id] = price
        quantity = session["cart"][product_id]
        total += price * quantity
    return render_template("cart.html", cart = session["cart"], names = names, prices = prices, total = total, imgs = imgs)


@app.route("/shop/<int:product_id>", methods = ["GET", "POST"])
def product(product_id):
    form = ReviewsForm()
    db = get_db()
    review = form.review.data
    user_id = session.get("user_id")
    product_name = db.execute("""SELECT name FROM products
                                 WHERE product_id = ?;""",(product_id,)).fetchone()
    product_img = db.execute("""SELECT img FROM products
                                WHERE product_id =?;""",(product_id,)).fetchone()
    product = db.execute("""SELECT * FROM products
                            WHERE product_id = ?;""", (product_id,)).fetchone()
    reviews = db.execute("""SELECT * FROM reviews;""").fetchall()
    if form.validate_on_submit():
        if user_id == None:
            return redirect(url_for("login"))
        else:
            db.execute("""INSERT INTO reviews (user_id,img,product_name, review)
                                VALUES (?,?,?,?);""", (str(user_id),product_img[0],product_name[0],str(review),))
            db.commit()
    return render_template("product.html", product = product, form = form, reviews = reviews)

@app.route("/finalisecart", methods = ["GET", "POST"])
def finalisecart():
    form = FinaliseCart()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        addressline1 = form.addressline1.data
        addressline2 = form.addressline2.data
        eircode = form.eircode.data
        if "cart" in session:
            session['cart'] = {}
        return render_template("shippingdetails.html", firstname = firstname, lastname = lastname, addressline1 = addressline1, addressline2 = addressline2, eircode = eircode)
    return render_template("finalisecart.html", form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        matching_user = db.execute(
            """SELECT * FROM users
                                               WHERE user_id = ?""",
            (user_id, )).fetchone()
        if matching_user is None:
            form.user_id.errors.append("Unknown user id!")
        elif not check_password_hash(matching_user["password"], password):
            form.password.errors.append("Incorrect password!")
        else:
            session.clear()
            session["user_id"] = user_id
            return redirect(url_for("index"))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



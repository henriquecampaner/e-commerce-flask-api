from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

login_manager = LoginManager()

db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = "login"
CORS(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)
    cart = db.relationship("CartItem", backref="user", lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(username=data.get("username")).first()

    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message": "Login successful"})

    return jsonify({"message": "Unauthorized. Invalid credentials"}), 401


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200


@app.route("/api/products/add", methods=["POST"])
@login_required
def add_product():
    data = request.json
    if "name" in data and "price" in data:
        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", ""),
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 200
    return jsonify({"message": "Missing name or price"}), 400


@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 404


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_products_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify(
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            }
        )
    return jsonify({"message": "Product not found"}), 404


@app.route("/api/products/update/<int:product_id>", methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.json
    if "name" in data:
        product.name = data["name"]

    if "price" in data:
        product.price = data["price"]

    if "description" in data:
        product.description = data["description"]

    db.session.commit()

    return jsonify({"message": "Product updated successfully"}), 200


@app.route("/api/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    print(products[0])

    product_list = []
    for product in products:
        product_data = {"id": product.id, "name": product.name, "price": product.price}
        product_list.append(product_data)

    return jsonify(product_list), 200


@app.route("/api/cart/add/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    user = User.query.get(int(current_user.id))

    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Product added to cart"})

    return jsonify({"message": "Product or User not found"}), 404


@app.route("/api/cart/remove/<int:product_id>", methods=["DELETE"])
@login_required
def delete_from_cart(product_id):
    cart_item = CartItem.query.filter_by(
        product_id=product_id, user_id=current_user.id
    ).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Product deleted from cart"})

    return jsonify({"message": "Failed to delete product from cart"}), 400


@app.route("/api/cart", methods=["GET"])
@login_required
def view_cart():
    user = User.query.get(int(current_user.id))

    if not user:
        return jsonify({"message": "User not found"}), 404

    cart_items = user.cart

    cart_list = []
    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        cart_list.append(
            {
                "id": cart_item.id,
                "user_id": cart_item.user_id,
                "product_id": cart_item.product_id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            }
        )
    return jsonify(cart_list), 200


@app.route("/api/cart/checkout", methods=["POST"])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart

    for cart_item in cart_items:
        db.session.delete(cart_item)

    db.session.commit()
    return jsonify({"message": "Checkout successful"})


if __name__ == "__main__":
    app.run(debug=True)

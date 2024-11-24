from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 800, "description": "A high-performance laptop."},
    {"id": 2, "name": "Smartphone", "price": 500, "description": "A latest-gen smartphone."},
    {"id": 3, "name": "Headphones", "price": 150, "description": "Noise-cancelling headphones."},
]

cart = []

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

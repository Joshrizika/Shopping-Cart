import sqlite3
from flask import Flask, session, render_template, redirect, request
from datetime import date
import time

app = Flask('app')
app.secret_key = "Amongus"

@app.route('/', methods=['GET', 'POST'])
def home():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM product")
  product_info = cursor.fetchall()
  cursor.execute("SELECT name FROM category")
  categories = cursor.fetchall()
  if request.method == 'POST':
    product_id = (str)(request.form['add_to_cart'])
    cursor.execute("SELECT name, description, price, stock, category FROM product WHERE id = ?", (product_id,))
    cart_info = cursor.fetchone()
    product_name = cart_info[0]
    product_description = cart_info[1]
    product_price = cart_info[2]
    product_stock = cart_info[3]
    product_category = cart_info[4]
    cart = session['cart']
    for item in cart:
      if item['id'] == product_id:
        if item['quantity']+1 > item['stock']:
          item['quantity'] = item['stock']
        else:
          item['quantity'] = item['quantity']+1
        session['cart'] = cart
        return ('', 204)
    added_item = {"id": product_id, "name": product_name, "description": product_description, "price": product_price, "stock": product_stock, "category": product_category, "quantity": 1}
    added_item_copy = added_item.copy()
    cart.append(added_item_copy)
    session['cart'] = cart
    return ('', 204)
  else:
    return render_template("home.html", products = product_info, categories = categories)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():

    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    error_message = ""

    if request.method == 'POST':
      email = request.form["email"]
      fname = request.form["fname"]
      lname = request.form["lname"]
      password = request.form["password"]
      if email == "":
        error_message = "Email cannot be empty"
        return render_template("create_account.html", error_message = error_message)
      elif fname == "":
        error_message = "First Name cannot be empty"
        return render_template("create_account.html", error_message = error_message)
      elif lname == "":
        error_message = "Last Name cannot be empty"
        return render_template("create_account.html", error_message = error_message)
      elif password == "":
        error_message = "Password cannot be empty"
        return render_template("create_account.html", error_message = error_message)
      cursor.execute ("SELECT email, password FROM users")
      users = cursor.fetchall()
      for user in users:
        if user["email"] == email:
          error_message = "Email Already in Use"
          return render_template("create_account.html", error_message = error_message)
        elif user["password"] == password:
          error_message = "Password Already Taken"
          return render_template("create_account.html", error_message = error_message)
      cursor.execute ("INSERT INTO users VALUES (?, ?, ?, ?);", (email, fname, lname, password))
      cursor.execute ("SELECT email, fname, lname, password FROM users WHERE email = ? AND password = ?", (email, password))
      user = cursor.fetchone()
      connection.commit()
      if user:
        session['email'] = user["email"]
        session['fname'] = user["fname"]
        session['lname'] = user["lname"]
        session['cart'] = []
        return redirect('/')
    return render_template("create_account.html", error_message = error_message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    errorMes = ""

    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    if request.method == 'POST':
      email = request.form["email"]
      password = request.form["password"]
      cursor.execute ("SELECT email, fname, lname, password FROM users WHERE email = ? AND password = ?", (email, password))
      user = cursor.fetchone()
      if user:
        session['email'] = user["email"]
        session['fname'] = user["fname"]
        session['lname'] = user["lname"]
        session['cart'] = []
        return redirect('/')
      else:
        errorMes = "Incorrect Email or password, please try again"
    return render_template("login.html", errorMes = errorMes)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
  session.clear()
  return redirect('/')

@app.route('/category_<category>', methods=['GET', 'POST'])
def category(category):
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM product WHERE category = ?", (category,))
  product_info = cursor.fetchall()
  cursor.execute("SELECT name FROM category")
  categories = cursor.fetchall()
  if request.method == 'POST':
    product_id = (str)(request.form['add_to_cart'])
    cursor.execute("SELECT name, price, stock FROM product WHERE id = ?", (product_id,))
    cart_info = cursor.fetchone()
    product_name = cart_info[0]
    product_price = cart_info[1]
    product_stock = cart_info[2]
    cart = session['cart']
    for item in cart:
      if item['id'] == product_id:
        item['quantity'] = item['quantity'] + 1
        session['cart'] = cart
        return ('', 204)
    added_item = {"id": product_id, "name": product_name, "price": product_price, "stock": product_stock, "quantity": 1}
    added_item_copy = added_item.copy()
    cart.append(added_item_copy)
    session['cart'] = cart
    return ('', 204)
  return render_template("home.html", products = product_info, categories = categories)

@app.route('/search', methods=['GET', 'POST'])
def search():
  query = "%"+request.args.get("query")+"%"
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM product WHERE name LIKE ?", (query,))
  product_info = cursor.fetchall()
  cursor.execute("SELECT name FROM category")
  categories = cursor.fetchall()
  if request.method == 'POST':
    product_id = (str)(request.form['add_to_cart'])
    cursor.execute("SELECT name, price, stock FROM product WHERE id = ?", (product_id,))
    cart_info = cursor.fetchone()
    product_name = cart_info[0]
    product_price = cart_info[1]
    product_stock = cart_info[2]
    cart = session['cart']
    for item in cart:
      if item['id'] == product_id:
        item['quantity'] = item['quantity'] + 1
        session['cart'] = cart
        return ('', 204)
    added_item = {"id": product_id, "name": product_name, "price": product_price, "stock": product_stock, "quantity": 1}
    added_item_copy = added_item.copy()
    cart.append(added_item_copy)
    session['cart'] = cart
    return ('', 204)
  return render_template("home.html", products = product_info, categories = categories)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
  cart = session['cart']
  for item in cart:
    quantity = request.args.get(item['id'])
    if not quantity == None:
      if (int)(quantity) > item['stock']:
        item['quantity'] = item['stock']
      else:
        item['quantity'] = (int)(quantity)
      session['cart'] = cart
  if request.method == 'POST':
    product_id = (str)(request.form['remove_from_cart'])
    if product_id == "everything":
      session['cart'] = []
      return render_template("cart.html", cart_products = session['cart'], error_message = "")
    for item in cart:
      if item['id'] == product_id:
        cart.remove(item)
        session['cart'] = cart
        return render_template("cart.html", cart_products = session['cart'], error_message = "")
  return render_template("cart.html", cart_products = session['cart'])

@app.route('/check_out', methods=['GET', 'POST'])
def check_out():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  orderitems = session['cart']
  error_message = ""
  if not orderitems:
    error_message = "Cannot Check Out an Empty Cart"
    return render_template("cart.html", cart_products = session['cart'], error_message = error_message)
  cursor.execute("SELECT COUNT(order_id) FROM orders")
  orderidint = (int)(cursor.fetchone()[0])+1
  order_id = str(orderidint).zfill(5)
  email = session['email']
  today = date.today()
  now = time.time()
  total_price = 0
  for item in orderitems:
    productid = item['id']
    stock = item['stock']
    quantity = item['quantity']
    new_stock = stock-quantity
    cursor.execute("UPDATE product SET stock = ? WHERE id = ?", (new_stock, productid))
    price = item['price']
    total_price+=(price*quantity)
    cursor.execute("SELECT COUNT(order_item_id) FROM order_item")
    order_item_id_int = (int)(cursor.fetchone()[0])+1
    order_item_id = str(order_item_id_int).zfill(5)
    cursor.execute("INSERT INTO order_item VALUES (?, ?, ?, ?, ?, ?)", (order_item_id, email, today, productid, order_id, quantity))
    connection.commit()
  cursor.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", (order_id, email, today, now, total_price))
  connection.commit()
  session['cart'] = []
  return redirect('/')
  
@app.route('/orders', methods=['GET', 'POST'])
def orders():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM orders WHERE customer_email = ? ORDER BY orders.time_ordered DESC", (session['email'],))
  orders = cursor.fetchall()
  cursor.execute("SELECT order_item.order_item_id, order_item.order_id, product.name, order_item.quantity, product.category, product.id FROM order_item CROSS JOIN orders ON order_item.order_id = orders.order_id CROSS JOIN product ON order_item.product_id = product.id WHERE order_item.customer_email = ?", (session['email'],))
  order_items = cursor.fetchall()
  return render_template("orders.html", orders = orders, order_items = order_items)

@app.route('/orders_asc', methods=['GET', 'POST'])
def orders_asc():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM orders WHERE customer_email = ? ORDER BY orders.time_ordered ASC", (session['email'],))
  orders = cursor.fetchall()
  cursor.execute("SELECT order_item.order_item_id, order_item.order_id, product.name, order_item.quantity, product.category, product.id FROM order_item CROSS JOIN orders ON order_item.order_id = orders.order_id CROSS JOIN product ON order_item.product_id = product.id WHERE order_item.customer_email = ?", (session['email'],))
  order_items = cursor.fetchall()
  return render_template("orders.html", orders = orders, order_items = order_items)

@app.route('/orders_desc', methods=['GET', 'POST'])
def orders_desc():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM orders WHERE customer_email = ? ORDER BY orders.time_ordered DESC", (session['email'],))
  orders = cursor.fetchall()
  cursor.execute("SELECT order_item.order_item_id, order_item.order_id, product.name, order_item.quantity, product.category, product.id FROM order_item CROSS JOIN orders ON order_item.order_id = orders.order_id CROSS JOIN product ON order_item.product_id = product.id WHERE order_item.customer_email = ?", (session['email'],))
  order_items = cursor.fetchall()
  return render_template("orders.html", orders = orders, order_items = order_items)

@app.route('/order-search', methods=['GET', 'POST'])
def ordersearch():
  orderquery = "%"+request.args.get("orderquery")+"%"
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM orders WHERE customer_email = ? ORDER BY orders.time_ordered DESC", (session['email'],))
  allorders = cursor.fetchall()
  cursor.execute("SELECT order_item.order_item_id, order_item.order_id, product.name, order_item.quantity, product.category, product.id FROM order_item CROSS JOIN orders ON order_item.order_id = orders.order_id CROSS JOIN product ON order_item.product_id = product.id WHERE order_item.customer_email = ? AND product.name LIKE ?", (session['email'], orderquery))
  order_items = cursor.fetchall()
  orders = []
  for item in order_items:
    item_orderid = item['order_id']
    for order in allorders:
      order_orderid = order['order_id']
      if item_orderid == order_orderid and order not in orders:
        orders.append(order)
  return render_template("orders.html", orders = orders, order_items = order_items)

app.run(host='0.0.0.0', port=8080)

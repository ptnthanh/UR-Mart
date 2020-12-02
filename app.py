# Import the Flask module from the flask package
from flask import Flask, Blueprint, render_template, request, session, redirect, url_for
from .models import Products
from . import db
from flask_login import login_required

app = Blueprint('app', __name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Create a "route" using a "decoration"
@app.route('/', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def index():
	filter_by = request.args.get("filter")
	products = Products.query.order_by(Products.dateAdded.desc())
	filter_label = "Newest"
	if filter_by == "low_to_high":
		products = Products.query.order_by(Products.originalPrice)
		filter_label = "Price (Low to High)"
	if filter_by == "high_to_low":
		products = Products.query.order_by(Products.originalPrice.desc())
		filter_label = "Price (High to Low)"
	return render_template('home.html', function='app.index', products=products, filter_by=filter_by, filter_label=filter_label)

@app.route('/computers_&_accessories', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def computers():
	filter_by = request.args.get("filter")
	products = Products.query.filter_by(category='Computers & Accessories').order_by(Products.dateAdded.desc())
	filter_label = "Newest"
	if filter_by == "low_to_high":
		products = Products.query.filter_by(category='Computers & Accessories').order_by(Products.originalPrice)
		filter_label = "Price (Low to High)"
	if filter_by == "high_to_low":
		products = Products.query.filter_by(category='Computers & Accessories').order_by(Products.originalPrice.desc())
		filter_label = "Price (High to Low)"
	return render_template('home.html', function = 'app.computers', products=products, filter_by=filter_by, filter_label=filter_label)

@app.route('/headphones_&_earbuds', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def headphones():
	filter_by = request.args.get("filter")
	products = Products.query.filter_by(category='Headphones & Earbuds').order_by(Products.dateAdded.desc())
	filter_label = "Newest"
	if filter_by == "low_to_high":
		products = Products.query.filter_by(category='Headphones & Earbuds').order_by(Products.originalPrice)
		filter_label = "Price (Low to High)"
	if filter_by == "high_to_low":
		products = Products.query.filter_by(category='Headphones & Earbuds').order_by(Products.originalPrice.desc())
		filter_label = "Price (High to Low)"
	return render_template('home.html', function = 'app.headphones', products=products, filter_by=filter_by, filter_label=filter_label)

@app.route('/create_items', methods=['GET', 'POST'])
@login_required
def create():
	if request.method == "POST":
		title = request.form['title']
		category = request.form['category']
		subcategory = request.form['subcategory']
		SKU = request.form['SKU']
		amount = request.form['amount']
		price = request.form['price']
		link = request.form['link']
		brand = request.form['brand']
		description = request.form['description']
		listing = Products(title=title, category=category, SKU=SKU, stockAmount=amount, originalPrice=price, imgLink=link, brand=brand, subcategory=subcategory, description=description)
		try:
			db.session.add(listing)
			db.session.commit()
			return redirect(url_for('app.create'))
		except:
			return render_template('error.html')
	else:
		return render_template('create.html')

@app.route('/update_items', methods=['GET', 'POST'])
@login_required
def table():
	products = Products.query.order_by(Products.id)
	return render_template('table.html', products=products)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
	delete = Products.query.get_or_404(id)
	try:
		db.session.delete(delete)
		db.session.commit()
		return redirect(url_for('app.table'))
	except:
		return render_template('error.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
	update = Products.query.get_or_404(id)
	if request.method == "POST":
		try:
			update.title = request.form['title']
			update.category = request.form['category']
			update.subcategory = request.form['subcategory']
			update.SKU = request.form['SKU']
			update.stockAmount = request.form['amount']
			update.originalPrice = request.form['price']
			update.imgLink = request.form['link']
			update.brand = request.form['brand']
			update.description = request.form['description']
			db.session.commit()
			return redirect(url_for('app.table'))
		except:
			return render_template('error.html')
	else:
		return render_template('update.html', update=update)




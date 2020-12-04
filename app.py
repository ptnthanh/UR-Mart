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

filters = ["Newest", "Price (Low to High)", "Price (High to Low)"]
filters.sort()

def get_category_func(category):
	temp = None
	if category == "Computers & Accessories": temp = 'app.computers'
	elif category == "Headphones & Earbuds": temp = 'app.earphones'
	return temp

def get_subcategory_func(subcategory):
	temp = None
	if subcategory == "Gaming Laptop": temp = 'app.glaptops'
	elif subcategory == "Laptop": temp = 'app.laptops'
	elif subcategory == "Computer Accessory": temp = 'app.accessories'
	elif subcategory == "Headphones": temp = 'app.headphones'
	elif subcategory == "Earbuds": temp = 'app.earbuds'
	return temp

# Create a "route" using a "decoration"
@app.route('/', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def index():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.order_by(Products.dateAdded.desc()).all()
	brands = Products.query.with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.index', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

@app.route('/computers_&_accessories', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def computers():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(category="Computers & Accessories").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(category="Computers & Accessories").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(category="Computers & Accessories", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(category="Computers & Accessories", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(category="Computers & Accessories").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(category="Computers & Accessories", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(category="Computers & Accessories").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.computers', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

@app.route('/computers_&_accessories/gaming_laptops', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def glaptops():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(subcategory="Gaming Laptop").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(subcategory="Gaming Laptop").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(subcategory="Gaming Laptop", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(subcategory="Gaming Laptop", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(subcategory="Gaming Laptop").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(subcategory="Gaming Laptop", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(subcategory="Gaming Laptop").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.glaptops', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

@app.route('/computers_&_accessories/laptops', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def laptops():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(subcategory="Laptop").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(subcategory="Laptop").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(subcategory="Laptop", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(subcategory="Laptop", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(subcategory="Laptop").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(subcategory="Laptop", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(subcategory="Laptop").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.laptops', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

@app.route('/computers_&_accessories/computer_accessory', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def accessories():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(subcategory="Computer Accessory").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(subcategory="Computer Accessory").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(subcategory="Computer Accessory", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(subcategory="Computer Accessory", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(subcategory="Computer Accessory").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(subcategory="Computer Accessory", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(subcategory="Computer Accessory").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.accessories', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)		

@app.route('/headphones_&_earbuds/headphones', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def headphones():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(subcategory="Headphones").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(subcategory="Headphones").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(subcategory="Headphones", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(subcategory="Headphones", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(subcategory="Headphones").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(subcategory="Headphones", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(subcategory="Headphones").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.headphones', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

@app.route('/headphones_&_earbuds/earbuds', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def earbuds():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(subcategory="Earbuds").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(subcategory="Earbuds").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(subcategory="Earbuds", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(subcategory="Earbuds", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(subcategory="Earbuds").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(subcategory="Earbuds", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(subcategory="Earbuds").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.earbuds', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

@app.route('/headphones_&_earbuds', methods=['GET', 'POST'])
# Create a Python function that will be executed at the decoration
def earphones():
	filter_by = "Newest"
	brand = "All"
	products = Products.query.filter_by(category="Headphones & Earbuds").order_by(Products.dateAdded.desc()).all()
	brands = Products.query.filter_by(category="Headphones & Earbuds").with_entities(Products.brand).distinct().all()
	brands = [i[0] for i in brands]
	brands.sort()
	if request.method == "GET":
		if request.args.get('filter') != None: filter_by = request.args.get('filter')
		if request.args.get('brand') != None: brand = request.args.get('brand')
	elif request.method == "POST":
		filter_by = request.form['filter']
		brand = request.form['brand']
	if filter_by == "Newest":
		if brand != "All": products = Products.query.filter_by(category="Headphones & Earbuds", brand=brand).order_by(Products.dateAdded.desc()).all()
	elif filter_by == "Price (Low to High)":
		if brand != "All": products = Products.query.filter_by(category="Headphones & Earbuds", brand=brand).order_by(Products.originalPrice).all()
		else: products = Products.query.filter_by(category="Headphones & Earbuds").order_by(Products.originalPrice).all()
	elif filter_by == "Price (High to Low)":
		if brand != "All": products = Products.query.filter_by(category="Headphones & Earbuds", brand=brand).order_by(Products.originalPrice.desc()).all()
		else: products = Products.query.filter_by(category="Headphones & Earbuds").order_by(Products.originalPrice.desc()).all()
	return render_template('home.html', function='app.earphones', products=products, brands=brands, filters=filters, filter_by=filter_by, brand=brand)

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
			return redirect(url_for('app.table'))
		except:
			return render_template('error.html')
	else:
		return render_template('create.html')

@app.route('/update_items', methods=['GET', 'POST'])
@login_required
def table():
	search = ""
	products = Products.query.order_by(Products.id)
	if request.method == "POST":
		search = request.form['search']
		products = Products.query.filter(Products.title.contains(search)).order_by(Products.id).all()
	return render_template('table.html', products=products)

@app.route('/delete/<string:SKU>', methods=['GET', 'POST'])
@login_required
def delete(SKU):
	delete = Products.query.filter_by(SKU=SKU).first()
	try:
		db.session.delete(delete)
		db.session.commit()
		return redirect(url_for('app.table'))
	except:
		return render_template('error.html')

@app.route('/update/<string:SKU>', methods=['GET', 'POST'])
@login_required
def update(SKU):
	update = Products.query.filter_by(SKU=SKU).first()
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

@app.route('/item/<string:SKU>', methods=['GET', 'POST'])
def item(SKU):
	item = Products.query.filter_by(SKU=SKU).first()
	category = get_category_func(item.category)
	subcategory = get_subcategory_func(item.subcategory)
	strings = item.description.split("(*)")
	return render_template('item.html', item=item, category=category, subcategory=subcategory, strings=strings)



import os
# Import the Flask module from the flask package
from flask import Flask, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, IntegerField, validators
# from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

# Instantiate the Flask class to the variable: app
app = Flask(__name__)
application = app
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True, nullable=False)
    category = db.Column(db.String(64), nullable=False)
    subcategory = db.Column(db.String(64), nullable=False)
    SKU = db.Column(db.String(64), nullable=False)
    stockAmount = db.Column(db.Integer)
    originalPrice = db.Column(db.Float)
    imgLink = db.Column(db.String(256), unique=True, nullable=False)
    dateAdded = db.Column(db.DateTime, default=datetime.now())
    brand = db.Column(db.String(64))
   
    def __repr__(self):
        return '<Product %r>' % self.id

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
	return render_template('home.html', function='index', products=products, filter_by=filter_by, filter_label=filter_label)

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
	return render_template('home.html', function = 'computers', products=products, filter_by=filter_by, filter_label=filter_label)

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
	return render_template('home.html', function = 'headphones', products=products, filter_by=filter_by, filter_label=filter_label)
	
@app.route('/create_items', methods=['GET', 'POST'])
def create():
	title = "Create Items (FOR TESTING)"
	if request.method == "POST":
		title = request.form['title']
		category = request.form['category']
		subcategory = request.form['subcategory']
		SKU = request.form['SKU']
		amount = request.form['amount']
		price = request.form['price']
		link = request.form['link']
		brand = request.form['brand']
		listing = Products(title=title, category=category, SKU=SKU, stockAmount=amount, originalPrice=price, imgLink=link, brand=brand, subcategory=subcategory)
		try:
			db.session.add(listing)
			db.session.commit()
			return redirect(url_for('create'))
		except:
			return "CANNOT ADD ITEMS!"
	else:
		return render_template('create.html', title=title)



from flask import render_template
from market.models import Item
from market import app

@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/market')
def get_product():
    items = Item.query.all()
    return render_template('market.html', items=items)


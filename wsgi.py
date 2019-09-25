# wsgi.py
from flask import Flask
from flask import jsonify
from flask import abort

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def getProducts():
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'LaGrosseRadio.tv' }
    ]
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:post_id>')
def getProduct(post_id):

    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'LaGrosseRadio.tv' },
        { 'id': 4, 'name': 'toto.tv' }
    ]

    index_products = len(PRODUCTS)
    index=0

    if post_id <= index_products:
        while index < index_products :
                PRODUCT = PRODUCTS[int(index)]
                index += 1
                if PRODUCT['id'] == post_id:
                    #print(PRODUCT)
                    return jsonify(PRODUCT)
    else:
        PRODUCT = {}
        abort (404)



